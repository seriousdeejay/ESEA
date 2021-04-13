<template>
    <div class="card p-mx-5 p-mb-5">
        <div class="p-d-flex p-jc-between p-m-2">
            <div>
                {{ dateFixer(campaign.open_survey_date, 'MMMM Do YYYY') }}
            </div>
            <div>
                {{ dateFixer(campaign.close_survey_date, 'MMMM Do YYYY') }}
            </div>
        </div>
        <ProgressBar :value="timeline" :showValue="true">
            <div v-if="campaigntimeleft > 0"> {{campaigntimeleft}} days left </div>
            <div v-else>This campaign has finished</div>
        </ProgressBar>
    </div>
    <br>
    <br>
    <div v-for="survey in eseaAccount.survey_response_by_survey" :key="survey.id" class="p-m-5">
        <ProgressBar :value="survey.current_response_rate + 10" :showValue="true">
            '{{survey.name}}' - Response Rate: {{survey.current_response_rate + 10}}%
        </ProgressBar>
    </div>
    <TabView>

        <TabPanel header="Surveys">
            <DataTable :value="eseaAccount.survey_response_by_survey" datakey="id" :rows="10" :paginator="true" :rowHover="true" v-model:filters="filters" filterDisplay="Menu" selectionMode="single" @row-select="gotoSurvey"
            paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown" :rowsPerPageOptions="[10,25,50]"
            currentPageReportTemplate="Showing {first} to {last} of {totalRecords} entries">
            <template #header>
                <div class="p-d-flex p-jc-between p-ai-center">
                    <h5 class="p-m-0">Surveys</h5>
                    <span class="p-input-icon-left">
                        <i class="pi pi-search" />
                        <InputText v-model="filters['global'].value" placeholder="Keyword Search" />
                    </span>
                    <div>
                        <SplitButton label="Tools" :model="items"></SplitButton>
                    </div>
                </div>
            </template>
            <Column field="name" header="Name" sortable />
            <Column field="stakeholdergroup" header="Stakeholder Group" />
            <Column field="questions" header="Questions" sortable />
            <Column field="respondees.length" header="Stakeholders" sortable />
            <Column field="responses" header="Responses" sortable />
            <Column field="current_response_rate" header="Response Rate" sortable>
                <template #body="{data}">
                    <ProgressBar :value="(data.current_response_rate)" :showValue="true" />
                </template>
            </Column>
            <Column field="required_response_rate" header="Response Rate Threshold" sortable>
                <template #body='{data}'>
                    {{data.required_response_rate}}%
                </template>
            </Column>
            <Column headerStyle="width: 15rem; text-align: center" bodyStyle="text-align: center; overflow: visible">
                <template #body="{data}">
                    <Button v-if="(data.stakeholdergroup === 'accountant')" :label="data.responses? 'Survey Results' : 'Fill in Survey'" type="button" icon="" class="p-button-success" @click="data.responses? goToResults(data) : goToSurveyFill(data)"  style="width: 200px" />
                    <Button v-else label="Import Employees" type="button" icon="pi pi-user-plus" @click="addEmployees(data)" style="width: 200px" />
                </template>
            </Column>
            </DataTable>
        </TabPanel>
        <TabPanel header="Report">
            d
        </TabPanel>
        <TabPanel header="Settings">
            <div class="p-col-8 p-fluid p-text-left p-p-5" style="width: 600px">

                    <div class="p-d-flex p-jc-between">
                        <Button label="Save ESEA Account Details" class="p-button-primary p-button-sm p-mr-5" @click="editCampaign" :disabled="false"/>
                        <Button label="Delete ESEA Account" class="p-button-danger p-button-sm p-ml-5" @click="deleteCampaignDialog = true" />
                    </div>
                </div>
        </TabPanel>
    </TabView>
    {{surveyy}}
    <Dialog v-model:visible="importEmployeesDialog" :style="{width: '900px'}" header="Import your stakeholders" :modal="true" class="p-fluid">
        <div class="p-d-flex p-jc-between p-ai-start p-p-5" style="border: 1px solid lightgrey;">
        <Listbox v-if="surveyy.respondees.length" v-model="s" :options="surveyy.respondees" :multiple="false"  optionLabel="name" :filter="true" listStyle="max-height:250px" style="width:15rem" filterPlaceholder="Search">
            <template #option="slotProps">
                <div class="country-item">
                    <div>{{slotProps.option.name}}</div>
                </div>
            </template>
        </Listbox>
        <div>
        <p>Import employees for the following survey: <span class="p-text-italic">'{{surveyy.name}}'</span>.</p>
        <FileUpload name="myfile" :customUpload="true" @uploader="onUpload" :fileLimit="1" accept=".csv" :maxFileSize="1000000">
            <template #empty>
                <p>Drag and drop your csv file here to upload.</p>
            </template>
        </FileUpload>
        </div>
        </div>
        <template #footer>
            <Button label="Remove window" icon="pi pi-times" class="p-button-text" @click="(importEmployeesDialog = false)"/>
        </template>
    </Dialog>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import { AxiosInstance } from '../../plugins/axios'
import { FilterMatchMode } from 'primevue/api'
import ProgressBar from 'primevue/progressbar'
import Listbox from 'primevue/listbox'
import SplitButton from 'primevue/splitbutton'
import dateFixer from '../../utils/datefixer'
import moment from 'moment'

export default {
    components: {
        ProgressBar,
        Listbox,
        SplitButton
    },
    data () {
        return {
            filters: {
                global: { value: null, matchMode: FilterMatchMode.CONTAINS }
            },
            columns: [
                { field: 'name', header: 'Name' },
                { field: 'method', header: 'Method' },
                // { field: 'description', header: 'Description' },
                { field: 'questions.length', header: 'Questions' },
                { field: 'stakeholders', header: 'Stakeholder group' }
            ],
            importEmployeesDialog: false,
            surveyy: null,
             items: [
                {
                    label: '- Send Message',
                    command: () => {
                        this.$toast.add({ severity: 'warn', summary: 'Delete', detail: 'Data Deleted', life: 3000 })
                    }
                },
                {
                    label: '- Send Reminder',
                    command: () => {
                        this.$toast.add({ severity: 'warn', summary: 'Delete', detail: 'Data Deleted', life: 3000 })
                    }
                }
            ]
        }
    },
    computed: {
        ...mapState('eseaAccount', ['eseaAccount']),
        ...mapState('survey', ['surveys']),
        ...mapState('campaign', ['campaign']),
        timeline () {
            const jsondate = new Date().toJSON()
            var currentdate = moment(jsondate, 'YYYY-MM-DD')
            var admission = moment(this.campaign.open_survey_date, 'YYYY-MM-DD')
            var discharge = moment(this.campaign.close_survey_date, 'YYYY-MM-DD')
            var progress = (admission.diff(currentdate, 'days') / admission.diff(discharge, 'days')) * 100
            return progress
        },
        campaigntimeleft () {
            const jsondate = new Date().toJSON()
            var currentdate = moment(jsondate, 'YYYY-MM-DD')
            var discharge = moment(this.campaign.close_survey_date, 'YYYY-MM-DD')
            var daysleft = (discharge.diff(currentdate, 'days'))
            return daysleft
        }
    },
    created () {
        this.initialize()
    },
    methods: {
        ...mapActions('survey', ['fetchSurveys']),
        ...mapActions('campaign', ['fetchCampaign']),
        dateFixer,
        async initialize () {
            this.fetchSurveys({ mId: this.eseaAccount.method.id })
            this.fetchCampaign({ nId: this.eseaAccount.network, id: this.eseaAccount.campaign })
        },
        addEmployees (data) {
            this.surveyy = data
            this.importEmployeesDialog = true
            if (data.id) {
                this.importEmployeesDialog = true
            }
        },
        async onUpload (event) {
            var formData = new FormData()
            formData.append('file', event.files[0])
            return new Promise((resolve, reject) => {
                AxiosInstance.post(`/import-employees/${this.$route.params.EseaAccountId || 0}/${this.surveyy.id}/`, formData) // esea account // survey
                .then(response => {
                    this.importDialog = false
                    this.$toast.add({ severity: 'success', summary: 'CSV uploaded', detail: 'Your csv was correctly uploaded.' })
                    this.initialize()
                resolve()
                })
                .catch(err => { reject(err) })
            })
        },
        async goToSurveyFill (data) {
            this.$router.push({ name: 'survey-fill-page', params: { uniquetoken: 'accountant' } })
        },
        goToSurvey (methodid, surveyid) {
            console.log(methodid)
            this.$router.push({ name: 'survey-fill-page', params: { uniquetoken: 0 } })
        },
        goToResults (data) {
            console.log(data)
            this.$router.push({ name: 'esea-account-report', params: { OrganisationId: this.$route.params.OrganisationId, EseaAccountId: this.eseaAccount.id } })
        }
    }
}

        // <!-- <TabPanel header="surveys">
        //     <DataTable ref="dt" autoLayout="false" :value="surveys" v-model:selection="selectedRows" selectionMode="single" dataKey="id" :loading="loading" @row-select="goToSurvey"
        //     :paginator="true" :rows="10" :filters="filters" paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
        //     :rowsPerPageOptions="[5,10,25]" currentPageReportTemplate="Showing {first} to {last} of {totalRecords} products" class="p-datatable-striped">

        //         <template #loading>
        //             Loading records, please wait...
        //         </template>
        //         <template # empty>
        //             empty
        //         </template>
        //         <Column
        //             v-for="column in columns"
        //             :key="column"
        //             :field="column.field"
        //             :header="column.header"
        //             ><template v-if="column.header === 'action'" #body="slotProps">
        //                 <Button v-if="surveyWithResponse" type="button" label="Results" class="p-button-raised p-button secondary" @click="goToSurveyResult(slotProps.data)" />
        //                 <Button v-else label="Participate"  @click="goToSurveyResult(slotProps.data)" />
        //             </template>
        //         </Column>
        //         <Column headerStyle="width: 20rem; text-align: center" bodyStyle="text-align: center; overflow: visible">
        //         <template #body>
        //             <Button label="Add Employees" type="button" icon="pi pi-user-plus"></Button>
        //         </template>
        //     </Column>

        //         <<Column field="name" header="Name"></Column>
        //         <Column v-if="false" field="description" header="Description"></Column>
        //         <Column field="questions.length" header="Questions"></Column>
        //         <Column field="method.name" header="Method"></Column>
        //         <Column field="stakeholders" header="Stakeholder group"></Column>
        //         <Column header="Action" headerStyle="width: 15%">
        //             <template #body="slotProps">
        //                 <Button v-if="surveyWithResponse" type="button" label="Results" class="p-button-raised p-button secondary" @click="goToSurveyResult(slotProps.data)" />
        //                 <Button v-else label="Participate"  @click="goToSurveyResult(slotProps.data)" />
        //             </template>
        //         </Column>
        //     </DataTable>
        //     {{surveys}}
        // </TabPanel> -->
</script>

<style lang="scss" scoped>
.p-splitbutton {
    width: 200px;
}
</style>
