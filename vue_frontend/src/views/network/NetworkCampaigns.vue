<template>
    <div class="p-field p-fluid"><InputText id="description" v-model="something" autofocus required="true" /></div>
    <div class="p-d-flex p-jc-between p-m-5">
        <Button label="New Campaign" icon="pi pi-plus" class="p-button-success p-d-flex p-mx-5" @click="createCampaignDialog = true" />
        <span class="p-input-icon-left">
            <i class="pi pi-search" /><InputText v-model="search" placeholder="Search..." />
        </span>
    </div>
    <Divider />
    <div v-if="campaigns.length" class="p-grid p-m-5">
        <div v-for="campaign in campaigns" :key="campaign.name" class="p-col-12 p-md-6 p-lg-4" style="width: 400px">
            <div class="p-p-3" :class="campaign.hover ? 'p-shadow-1 p-m-1' : 'p-shadow-1 p-m-0'" style="border-radius: 3px" :style="(campaign.hover ? styleObject : '')"  @mouseover="campaign.hover=true" @mouseleave="campaign.hover = false" @click="goToCampaign(campaign)">
                    <p class="p-text-light">{{ dateFixer(campaign.open_survey_date, 'MMMM Do YYYY') }} - {{ dateFixer(campaign.close_survey_date, 'MMMM Do YYYY') }}</p> <!-- MM/Do/YYYY' -->
                    <!-- <span class="p-text-italic">{{ dateFixer(campaign.close_survey_date, 'MMMM Do YYYY') }}</span> -->
                <img :src="campaign.image" alt="Campaign Image" style="max-width: 150px; max-height: 150px; border-radius: 50%;" format="PNG">
                 <p class="p-text-italic">{{campaign.name}}</p>

                <Divider />
                <div class="p-text-left p-ml-3">
                    <p>Method: <span class="p-text-bold">{{campaign.method}}</span></p> <!-- Should be method name instead of pk! -->
                    <p>Participating Organisations: <span class="p-text-bold">{{campaign.organisation_accounts.length}}</span></p>
                </div>
            </div>
        </div>
    </div>
    <div v-else class="p-text-italic">There are no campaigns to display, create one!</div>

    <Dialog v-model:visible="createCampaignDialog" style="width: 700px" contentStyle="height: 600px" header="Campaign Details" class="p-fluid p-text-left" modal="false" dismissableMask="true">
        <div class="p-field ">
            <div class="p-field p-fluid"><InputText id="description" v-model="something" autofocus required="true" /></div>
            <label for="name">Name<span style="color:red">*</span></label>
            <InputText id="name" v-model.trim="campaignForm.name" required="true" :class="{'p-invalid': submitted && !campaignForm.name}" />
            <small class="p-error" v-if="submitted && !campaignForm.name">A name is required.</small>
        </div>

        <div class="p-grid">
        <div class="p-field p-col-6">
            <label for="method">Method<span style="color:red">*</span></label>
            <Dropdown id="method" v-model="campaignForm.method" :options="methods" optionLabel="name" optionValue="id" placeholder="Select a Method" :class="{'p-invalid': submitted && !campaignForm.method}" />
            <small class="p-error" v-if="submitted && !campaignForm.method">A method is required.</small>
        </div>

        <div class="p-field p-col-6">
            <label for="organisations">Organisations</label>
            <MultiSelect id="organisations" v-model="selectedOrganisations" :options="organisations" optionLabel="name" placeholder="Select Organisations" :filter="true" class="multiselect-custom">
                <template #value="slotProps">
                    <div v-for="option of slotProps.value" :key="option.code">
                        <div>{{option.name}}</div>
                    </div>
                    <template v-if="!slotProps.value || slotProps.value.length === 0">
                        Select Organisations
                    </template>
                </template>
                <template #option="slotProps">
                    <div class="country-item">
                        <div>{{slotProps.option.name}}</div>
                    </div>
                </template>
            </MultiSelect>
        </div>
        </div>

        <div class="p-grid">
        <div class="p-field p-col-6 p-m-0">
            <label for="opendate">Opening Date</label>
            <Calendar id="opendate" v-model="campaignForm.open_survey_date" placeholder="Calendar" appendTo="body" :showTime="true" :showIcon="true" />

        </div>
        <div class="p-field p-col-6">
            <label for="enddate">Closing Date</label>
            <Calendar id="enddate" v-model="campaignForm.close_survey_date" placeholder="Calendar" appendTo="body" showTime="true" :showIcon="true" />
        </div>
        </div>
        <div class="p-field">
            <label for="description">Description</label>
            <Textarea id="description" v-model="something" required="true" rows="3" cols="20" />
        </div>
        <div class="p-field">
            <label for="message">Message to Organisations</label>
            <Textarea id="message" v-model="something" required="true" rows="3" cols="20" />
        </div>
        <template #footer>
            <Button label="Cancel" icon="pi pi-times" class="p-button-text" @click="createCampaignDialog = false"/>
            <Button label="Save" icon="pi pi-check" class="p-button-text" @click="createNewCampaign" :disabled="submitted && (!campaignForm.name || !campaignForm.method)" />
        </template>
    </Dialog>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import Calendar from 'primevue/calendar'
import Dropdown from 'primevue/dropdown'
import MultiSelect from 'primevue/multiselect'
import dateFixer from '../../utils/datefixer'

export default {
    components: {
        Calendar,
        Dropdown,
        MultiSelect
    },
    data () {
        return {
            campaignForm: {
                name: null,
                network: this.$route.params.NetworkId,
                method: null,
                organisations: [],
                open_survey_date: new Date(),
                close_survey_date: new Date()
            },
            hover: false,
            styleObject: { backgroundColor: '#EFEEEE' },
            createCampaignDialog: false,
            submitted: false,
            selectedOrganisations: null
        }
    },
    computed: {
        ...mapState('network', ['network']),
        ...mapState('method', ['methods']),
        ...mapState('campaign', ['campaigns', 'campaign']),
        organisations () {
            var dict = []
            this.network.organisations.forEach(org => dict.push({ name: org }))
            return dict
        }
    },
    created () {
        this.initialize()
    },
    methods: {
        ...mapActions('campaign', ['fetchCampaigns', 'createCampaign', 'setCampaign']),
        dateFixer,
        async initialize () {
            this.campaignForm.close_survey_date = new Date(this.campaignForm.close_survey_date.setDate(this.campaignForm.open_survey_date.getDate() + 30))
            await this.fetchCampaigns({ nId: this.$route.params.NetworkId })
            this.selectedOrganisations = this.organisations
        },
        async createNewCampaign () {
            this.submitted = false
            if (this.campaignForm.name && this.campaignForm.method) {
                for (var index in this.selectedOrganisations) {
                    this.campaignForm.organisations.push(this.selectedOrganisations[index].name)
                }
                await this.createCampaign({ nId: this.$route.params.NetworkId, data: this.campaignForm })
                this.$router.push({ name: 'networkcampaign', params: { NetworkId: this.$route.params.NetworkId, CampaignId: this.campaign.id } })
                this.createCampaignDialog = false
            }
            this.submitted = true
        },
        async goToCampaign (campaign) {
            await this.setCampaign(campaign)
            this.$router.push({ name: 'networkcampaign', params: { CampaignId: campaign.id } })
        }
    }

}
</script>
