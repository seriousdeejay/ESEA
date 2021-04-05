<template>
    <Toolbar class="p-mb-4">
                <template #left>
                    <Button label="New" icon="pi pi-plus" class="p-button-success p-mr-2" @click="createCampaignDialog = true" />
                    <Button label="Delete" icon="pi pi-trash" class="p-button-danger" @click="confirmDeleteSelected" :disabled="!selectedProducts || !selectedProducts.length" />
                </template>

                <template #right>
                    <FileUpload mode="basic" accept="image/*" :maxFileSize="1000000" label="Import" chooseLabel="Import" class="p-mr-2 p-d-inline-block" />
                    <Button label="Export" icon="pi pi-upload" class="p-button-help" @click="exportCSV($event)"  />
                </template>
    </Toolbar>
    {{campaign}}
    <div class="p-grid p-m-5">
        <div v-for="campaign in campaigns" :key="campaign.name" class="p-col-12 p-md-6 p-lg-4" style="width: 450px">
            <div class="p-p-3" :class="campaign.hover ? 'p-shadow-10 p-m-1' : 'p-shadow-5 p-m-2'" style="border-radius: 3px" :style="(campaign.hover ? styleObject : '')"  @mouseover="campaign.hover=true" @mouseleave="campaign.hover = false" @click="goToCampaign(campaign)">
                <h3>{{campaign.name}}</h3>
                <Divider />
                <div class="p-text-left p-ml-5">
                    <p>Method: <span class="p-text-bold">{{campaign.method}}</span></p>
                    <p>Participating Organisations: <span class="p-text-bold">{{campaign.organisation_accounts.length}}</span></p>
                </div>
                <Divider />
                <div class="p-d-flex p-jc-between p-mx-2">
                    <p>Opening on: <span class="p-text-bold">{{ dateFixer(campaign.open_survey_date, 'MM/DD/YYYY') }}</span></p>
                    <!-- If closing data has passed  closed on :-->
                    <p>Closing on: <span class="p-text-bold">{{ dateFixer(campaign.close_survey_date) }}</span></p>
                </div>
            </div>
        </div>
    </div>

    <Dialog v-model:visible="createCampaignDialog" style="width: 600px" contentStyle="height: 400px" header="Campaign Details" class="p-fluid p-text-left" baseZIndex="0">
        <div class="p-field ">
            <label for="name">Name</label>
            <InputText id="name" v-model.trim="campaignForm.name" required="true" autofocus :class="{'p-invalid': submitted && !campaignForm.name}" />
            <!-- @blur="updateCampaignForm({ name: $event.target.value })" /> -->
            <small class="p-error" v-if="submitted && !campaignForm.name">A name is required.</small>

        </div>
        <div class="p-field">
            <label for="method">Method</label>
            <Dropdown id="method" v-model="campaignForm.method" :options="methods" optionLabel="name" optionValue="name" placeholder="Select a Method" :class="{'p-invalid': submitted && !campaignForm.method}" />
            <small class="p-error" v-if="submitted && !campaignForm.method">A method is required.</small>
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
        <!-- <div class="p-field">
            <label for="description">Description</label>
            <Textarea id="description" v-model="something" required="true" rows="3" cols="20" />
        </div> -->
        <template #footer>
            <Button label="Cancel" icon="pi pi-times" class="p-button-text" @click="createCampaignDialog = false"/>
            <Button label="Save" icon="pi pi-check" class="p-button-text" @click="createNewCampaign" :disabled="submitted && (!campaignForm.name || !campaignForm.method)" />
        </template>
    </Dialog>
</template>

<script>
import Calendar from 'primevue/calendar'
import Dropdown from 'primevue/dropdown'
import { mapActions, mapState } from 'vuex'
import dateFixer from '../../utils/datefixer'

export default {
    components: {
        Calendar,
        Dropdown
    },
    data () {
        return {
            // campaigns: [
            //     { name: 'BIA 2019', method: 'Method 1', required: true, open_survey_date: '04-15-2019', close_survey_date: '05-15-2019', description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ', hover: false },
            //     { name: 'BIA 2020', method: 'Method 1', required: true, open_survey_date: '04-15-2020', close_survey_date: '05-15-2020', description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ', hover: true },
            //     { name: 'BIA 2021', method: 'Method 1', required: true, open_survey_date: '04-15-2021', close_survey_date: '05-15-2021', description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ', hover: false },
            //     { name: 'FTSF 2020', method: 'Method 1', required: true, open_survey_date: '04-15-2020', close_survey_date: '05-15-2020', description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ', hover: false }
            // ],
            campaignForm: {
                name: null,
                network: this.$route.params.NetworkId,
                method: null,
                open_survey_date: new Date(),
                close_survey_date: new Date()
            },
            hover: false,
            styleObject: { backgroundColor: '#EFEEEE' },
            createCampaignDialog: false,
            submitted: false
        }
    },
    computed: {
        ...mapState('method', ['methods']),
        ...mapState('campaign', ['campaigns', 'campaign'])
    },
    created () {
        this.initialize()
    },
    methods: {
        dateFixer,
        ...mapActions('campaign', ['fetchCampaigns', 'createCampaign', 'setCampaign']),
        async initialize () {
            this.campaignForm.close_survey_date = new Date(this.campaignForm.close_survey_date.setDate(this.campaignForm.open_survey_date.getDate() + 30))
            await this.fetchCampaigns({ nId: this.$route.params.NetworkId })
        },
        async createNewCampaign () {
            this.submitted = false
            console.log(typeof this.campaignForm.close_survey_date)
            if (this.campaignForm.name && this.campaignForm.method) {
                await this.createCampaign({ nId: this.$route.params.NetworkId, data: this.campaignForm })
                console.log('saved')
            }
            this.createCampaignDialog = false
            this.submitted = true
            this.$router.push({ name: 'networkcampaign', params: { NetworkId: this.$route.params.NetworkId, CampaignId: this.campaign.id } })
        },
        async goToCampaign (campaign) {
            await this.setCampaign(campaign)
            console.log(campaign)
            this.$router.push({ name: 'networkcampaign', params: { CampaignId: campaign.id } })
        }
    }

}
</script>