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

    <div class="p-grid p-m-5">
        <div v-for="campaign in campaigns" :key=campaign.name class="p-col-12 p-md-6 p-lg-4" style="width: 450px">
            <div class="p-p-3" :class="campaign.hover ? 'p-shadow-10 p-m-1' : 'p-shadow-5 p-m-2'" style="border-radius: 3px" :style="(campaign.hover ? styleObject : '')"  @mouseover="campaign.hover=true" @mouseleave="campaign.hover = false" @click="goToCampaign(campaign)">
                <h3>{{campaign.name}}</h3>
                <Divider />
                <p class="p-text-justify p-p-2">{{campaign.description}}</p>
                <Divider />
                <div class="p-d-flex p-jc-between p-mx-2">
                    <p>Opening on: <span class="p-text-bold">{{campaign.open_survey_date}}</span></p>
                    <!-- If closing data has passed  closed on :-->
                    <p>Closing on: <span class="p-text-bold">{{campaign.close_survey_date}}</span></p>
                </div>
            </div>
        </div>
    </div>

    <Dialog v-model:visible="createCampaignDialog" style="width: 600px" contentStyle="height:800px" header="Campaign Details" class="p-fluid p-text-left" baseZIndex="0">
        <div class="p-field ">
            <label for="name">Name</label>
            <InputText id="name" v-model.trim="something" required="true" autofocus :class="{'p-invalid': submitted && !something}" />
            <!-- @blur="updateCampaignForm({ name: $event.target.value })" /> -->
            <small class="p-error" v-if="submitted && !network.name">Name is required.</small>
        </div>
        <div class="p-grid">
        <div class="p-field p-col-7 p-m-0">
            <label for="opendate">Opening Date</label>
            <Calendar id="opendate" v-model="startdate" placeholder="Calendar" :showTime="true" :showIcon="true" />
            <!-- <label for="ispublic">Should this network be public? </label> -->
            <!-- <SelectButton id="ispublic" v-model="boolChoice" required="true" :options="ispublicbool"
            @blur="updateCammpaignForm({ ispublic: boolChoice })" /> -->
        </div>
        <div class="p-field p-col-7">
            <label for="enddate">Closing Date</label>
            <Calendar id="enddate" v-model="enddate" placeholder="Calendar" :showTime="true" :showIcon="true" />
            <!-- <label for="ispublic">Should this network be public? </label> -->
            <!-- <SelectButton id="ispublic" v-model="boolChoice" required="true" :options="ispublicbool"
            @blur="updateCammpaignForm({ ispublic: boolChoice })" /> -->
        </div>
        </div>
        <div class="p-field">
            <label for="description">Description</label>
            <Textarea id="description" v-model="something" required="true" rows="3" cols="20" />
            <!-- @blur="updateCampaignForm({ description: $event.target.value })" /> -->
        </div>
        <div class="p-field">
            <label for="method">Method</label>
            <Dropdown id="method" v-model="campaignmethod" :options="methods" optionLabel="name" optionValue="id" placeholder="Select a Method" />
        </div>
        {{startdate}} {{campaignmethod}}
        <template #footer>
            <Button label="Cancel" icon="pi pi-times" class="p-button-text" @click="createCampaignDialog = false"/>
            <Button label="Save" icon="pi pi-check" class="p-button-text" @click="something" disabled="" />
        </template>
    </Dialog>
</template>

<script>
import Calendar from 'primevue/calendar'
import Dropdown from 'primevue/dropdown'
import { mapState } from 'vuex'
export default {
    components: {
        Calendar,
        Dropdown
    },
    data () {
        return {
            campaigns: [
                { name: 'BIA 2019', method: 'Method 1', required: true, open_survey_date: '04-15-2019', close_survey_date: '05-15-2019', description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ', hover: false },
                { name: 'BIA 2020', method: 'Method 1', required: true, open_survey_date: '04-15-2020', close_survey_date: '05-15-2020', description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ', hover: true },
                { name: 'BIA 2021', method: 'Method 1', required: true, open_survey_date: '04-15-2021', close_survey_date: '05-15-2021', description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ', hover: false },
                { name: 'FTSF 2020', method: 'Method 1', required: true, open_survey_date: '04-15-2020', close_survey_date: '05-15-2020', description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ', hover: false }
            ],
            hover: false,
            styleObject: { backgroundColor: '#EFEEEE' },
            createCampaignDialog: false,
            startdate: null,
            enddate: null,
            campaignmethod: null
        }
    },
    computed: {
        ...mapState('method', ['methods'])
    },
    created () {
        this.initialize()
    },
    methods: {
        initialize () {
        },
        goToCampaign (campaign) {
            console.log(campaign)
        }
    }

}
</script>
