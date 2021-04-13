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
    <TabView style="height: 1000px">
        <TabPanel header="Method">
            <h4>Method: <span class="p-text-light p-text-italic">'{{method.name}}'</span></h4>
            <h4>Description: <span class="p-text-light p-text-italic">'{{method.description}}'</span></h4>
            <Button label="Go to Method" @click="goToMethod" />

        </TabPanel>
        <TabPanel header="ESEA Accounts" style="background-color: black;">
            <DataTable :value="eseaAccounts" datakey="id" :rows="10" :paginator="true" :rowHover="true" v-model:filters="filters" filterDisplay="menu" selectionMode="single" @row-select="goToEseaAccount" class="p-datatable-gridlines p-datatable-striped p-datatable-sm"
            paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown" :rowsPerPageOptions="[10,25,50]"
                    currentPageReportTemplate="Showing {first} to {last} of {totalRecords} entries">
                <template #header>
                    <div class="p-d-flex p-jc-between p-ai-center">
                        <h5 class="p-m-0">ESEA Accounts</h5>
                        <span class="p-input-icon-left">
                            <i class="pi pi-search" />
                            <InputText v-model="filters['global'].value" placeholder="Keyword Search" />
                        </span>
                        <div>
                            <Button label="Tool Menu" @click="toggle" />    <!-- aria-haspopup="true" aria-controls="overlay_menu" -->
                            <Menu id="overlay_menu" ref="menu" :model="items" :popup="true" />
                        </div>
                    </div>
                </template>
                <Column field="organisation" header="Organisation" sortable>
                    <template #filter="{filterModel}">
                        <InputText type="text" v-model="filterModel.value" class="p-column-filter" placeholder="Search by name"/>
                    </template>
                </Column>
                <Column field="sufficient_responses" header="Sufficient Responses" sortable />
                <Column field="all_respondents" header="Stakeholders" sortable />
                <Column field="all_responses.length" header="Responses" sortable />
                <Column field="response_rate" header="Response Rate" sortable :showFilterMatchModes="false" style="min-width: 10rem">
                        <template #body="{data}">
                            <ProgressBar :value="data.response_rate" :showValue="true" />
                        </template>
                        <template #filter="{filterModel}">
                            <Slider v-model="filterModel.value" range class="p-m-3"></Slider>
                            <div class="p-d-flex p-ai-center p-jc-between p-px-2">
                                <span>{{filterModel.value ? filterModel.value[0] : 0}}</span>
                                <span>{{filterModel.value ? filterModel.value[1] : 100}}</span>
                            </div>
                        </template>
                </Column>
                <Column header="Report" headerStyle="width: 4rem; text-align: center" bodyStyle="text-align: center; overflow: visible">
                    <template #body="data">
                        <Button @click="goToReport(data)" icon="pi pi-file-pdf" :class="data.sufficient_responses? 'p-button-success' : 'p-button-danger'"></Button>
                    </template>
                </Column>
            </DataTable>
        </TabPanel>
        <TabPanel header="Settings">
            <div class="p-grid">
                <div class="p-col-8 p-fluid p-text-left p-p-5" style="width: 600px">
                    <div class="p-field p-grid">
                        <label for="name" class="p-col-fixed" style="width: 200px">Name</label>
                        <InputText id="name" v-model.trim="campaign.name" required="true" autofocus :class="{'p-invalid': submitted && !campaign.name}" class="p-col"/>
                        <small class="p-error" v-if="submitted && !campaign.name">A name is required.</small>

                    </div>
                    <div class="p-field p-grid">
                        <label for="method" class="p-col-fixed" style="width: 200px">Method</label>
                        <Dropdown id="method" v-model="campaign.method" :options="methods" optionLabel="name" optionValue="name" placeholder="Select a Method" :class="{'p-invalid': submitted && !campaign.method}" class="p-col" />
                        <small class="p-error" v-if="submitted && !campaign.method">A method is required.</small>
                    </div>
                    <div class="p-field p-grid">
                        <label for="opendate" class="p-col-fixed" style="width: 200px">Opening Date</label>
                        <Calendar id="opendate" v-model="campaign.open_survey_date" placeholder="Calendar" appendTo="body" :showTime="true" :showIcon="true" class="p-col p-p-0" />
                        </div>
                    <div class="p-field p-grid">
                        <label for="enddate" class="p-col-fixed" style="width: 200px">Closing Date</label>
                        <Calendar id="enddate" v-model="campaign.close_survey_date" placeholder="Calendar" appendTo="body" showTime="true" :showIcon="true" class="p-col p-p-0" />
                    </div>

                    <div class="p-field p-grid">
                        <label for="description" class="p-col-fixed" style="width: 200px">Description</label>
                        <Textarea id="description" v-model="something" required="true" rows="3" cols="20" class="p-col" />
                    </div>

                    <div class="p-field p-grid">
                        <label for="reminder" class="p-col-fixed" style="width: 200px">Respondent reminder before deadline (in days)</label>
                        <InputNumber id="inputnumber" v-model="reminder" :min=1 class="p-col p-p-0"/>
                    </div>
                    <div class="p-d-flex p-jc-between">
                        <Button label="Save Campaign Details" class="p-button-primary p-button-sm p-mr-5" @click="editCampaign" :disabled="false"/>
                        <Button label="Delete Campaign" class="p-button-danger p-button-sm p-ml-5" @click="deleteCampaignDialog = true" />
                    </div>
                </div>
                <Divider layout="vertical" class="p-col-1"/>
                <div class="p-col p-p-5">
                    <DataTable :value="campaign.organisation_accounts" datakey="id" :rows="10" :paginator="true" :rowHover="true" v-model:filters="filters" filterDisplay="menu" v-model:selection="selectedOrganisations"  selectionMode="multiple" class="p-datatable-gridlines p-datatable-striped p-datatable-sm"
                    paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown" :rowsPerPageOptions="[10,25,50]"
                    currentPageReportTemplate="Showing {first} to {last} of {totalRecords} entries">
                        <template #header>
                            <div class="p-d-flex p-jc-between p-ai-center">
                                <h5 class="p-m-0">ESEA Accounts</h5>
                                <span class="p-input-icon-left">
                                    <i class="pi pi-search" />
                                    <InputText v-model="filters['global'].value" placeholder="Keyword Search" />
                                </span>
                                <div>
                                    <Button @click="(addOrganisationsDialog = true && addableOrganisations())" label="Add" class="p-button-success p-mr-2" />
                                    <Button @click="removeOrganisationsDialog = true" label="Remove" class="p-button-danger" />
                                </div>
                            </div>
                        </template>
                        <Column field="organisation"></Column>
                    </DataTable>
                </div>
            </div>
        </TabPanel>
    </TabView>

    <Dialog v-model:visible="removeOrganisationsDialog" :style="{width: '500px'}" header="Removal confirmation" :modal="true" dismissableMask="true">
        <div v-if="selectedOrganisations.length">
            <span>Are you sure you want to <b>remove</b> these from your campaign?</span>
            <div v-for="item in selectedOrganisations" :key=item.name class="p-shadow-2 p-mt-5 p-p-3">{{item.organisation}}</div>
        </div>
        <div v-else>
            You haven't selected any organisations.
        </div>
        <template #footer>
            <div v-if="selectedOrganisations.length">
                <Button label="No" icon="pi pi-times" class="p-button-text" @click="(removeOrganisationsDialog = false) && (selectedRows = [])"/>
                <Button label="Yes" icon="pi pi-check" class="p-button-text" @click="removeOrganisations()" />
            </div>
            <div v-else>
                <Button label="Ok" class="p-button-text" @click="removeOrganisationsDialog = false" />
                </div>
        </template>
    </Dialog>

    <Dialog v-model:visible="addOrganisationsDialog" :style="{width: '500px'}" :modal="true" dismissableMask="true">
        <div class="p-grid">
            <MultiSelect id="organisations" v-model="chosenOrganisations" :options="organisations" optionLabel="name" placeholder="Select Organisations" :filter="true" class="multiselect-custom p-col-12 p-mt-2">
                <template #value="slotProps">
                    <div v-for="option of slotProps.value" :key="option.id">
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
        <template #footer>
                <Button label="Add Selected Organisations" icon="pi pi-plus" @click="(addOrganisationsDialog = false && addOrganisations())"/>
                <Button label="Cancel" icon="pi pi-check" class="p-button-text" @click="addOrganisationsDialog = false" />
        </template>
    </Dialog>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import { FilterMatchMode, FilterOperator } from 'primevue/api'
import ProgressBar from 'primevue/progressbar'
import Slider from 'primevue/slider'
import Calendar from 'primevue/calendar'
import Dropdown from 'primevue/dropdown'
import MultiSelect from 'primevue/multiselect'
import dateFixer from '../../utils/datefixer'
import moment from 'moment'

export default {
    components: {
        Calendar,
        Dropdown,
        ProgressBar,
        Slider,
        MultiSelect
    },
    data () {
        return {
            filters: {
                global: { value: null, matchMode: FilterMatchMode.CONTAINS },
                organisation: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
                // organisation: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
                'country.name': { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
                representative: { value: null, matchMode: FilterMatchMode.IN },
                date: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.DATE_IS }] },
                balance: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }] },
                status: { operator: FilterOperator.OR, constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }] },
                all_response_rate: { value: null, matchMode: FilterMatchMode.BETWEEN },
                verified: { value: null, matchMode: FilterMatchMode.EQUALS }
            },
            reminder: 1,
            items: [
                {
                    label: '- Send Message',
                    command: () => {
                        console.log('Send Message')
                        this.$toast.add({ severity: 'warn', summary: 'Delete', detail: 'Data Deleted', life: 3000 })
                    }
                },
                {
                    label: '- Send Reminder',
                    command: () => { this.$toast.add({ severity: 'warn', summary: 'Delete', detail: 'Data Deleted', life: 3000 }) }
                },
                {
                    label: '- Sample Test',
                    command: () => { this.$toast.add({ severity: 'warn', summary: 'Delete', detail: 'Data Deleted', life: 3000 }) }
                },
                {
                    label: '- Add Organisations',
                    command: () => { this.$toast.add({ severity: 'success', summary: 'Updated', detail: 'Data Updated', life: 3000 }) }
                },
                {
                    label: '- Delete Organisations',
                    command: () => { this.$toast.add({ severity: 'warn', summary: 'Delete', detail: 'Data Deleted', life: 3000 }) }
                }
            ],
            selectedOrganisations: [],
            removeOrganisationsDialog: false,
            chosenOrganisations: null,
            addOrganisationsDialog: false
        }
    },
    computed: {
        ...mapState('campaign', ['campaign']),
        ...mapState('eseaAccount', ['eseaAccounts', 'eseaAccount']),
        ...mapState('method', ['methods', 'method']),
        ...mapState('organisation', ['organisations']),
        timelinedates () {
            var datearr = []
            datearr.push({ date: this.campaign.open_survey_date, name: 'openingdate' })
            datearr.push({ date: this.campaign.close_survey_date, name: 'closingdate' })
            return datearr
        },
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
        ...mapActions('eseaAccount', ['fetchEseaAccounts', 'setEseaAccount']),
        ...mapActions('method', ['fetchMethod']),
        ...mapActions('organisation', ['fetchOrganisations']),
        dateFixer,
        async initialize () {
            this.boolChoice = { name: 'Public', value: true }
            await this.fetchEseaAccounts({ nId: this.$route.params.NetworkId, cId: this.$route.params.CampaignId })
            await this.fetchMethod({ id: this.campaign.method })
        },
        toggle (event) {
            this.$refs.menu.toggle(event)
        },
        async addableOrganisations () {
            await this.fetchOrganisations({ query: `?network=${this.network.id}` })
        },
        async addOrganisations () {
            if (this.chosenOrganisations) {
                // Add Organisation to Campaign
            }
        },
        async goToEseaAccount (event) {
            await this.setEseaAccount(event.data)
            this.$router.push({ name: 'networkeseaaccount', params: { cId: this.campaign.id, EseaAccountId: event.data.id } })
        },
        async goToReport (event) {
            await this.setEseaAccount(event.data)
            this.$router.push({ name: 'esea-account-report', params: { OrganisationId: `${event.data.organisation}`, EseaAccountId: event.data.id } })
            console.log(event.data)
        },
        async goToMethod () {
            this.$router.push({ name: 'methoddetails', params: { id: this.campaign.method } })
        }
    }
}
</script>

<style scoped>
.p-splitbutton {
    width: 200px;
}
.custom-marker {
    display: flex;
    width: 2rem;
    height: 2rem;
    align-items: center;
    justify-content: center;
    color: #ffffff;
    border-radius: 50%;
    z-index: 1;
}

::v-deep(.p-timeline-event-content)
::v-deep(.p-timeline-event-opposite) {
    line-height: 1;
}

@media screen and (max-width: 960px) {
    ::v-deep(.customized-timeline) {
            .p-timeline-event:nth-child(even) {
                flex-direction: row !important;

                .p-timeline-event-content {
                    text-align: left !important;
                }
            }

            .p-timeline-event-opposite {
                flex: 0;
            }

            .p-card {
                margin-top: 1rem;
            }
        }
}
.p-tabview >>> .p-tabview-panels {
    background-color: #F8F9FA;
    border: 1px dotted lightgrey;
}
</style>
