<template>
<!--
            <DataTable ref="dt" :value="organisations" v-model:selection="selectedOrganisations" selectionMode="single" dataKey="id" @row-select="goToOrganisation"
            :paginator="true" :rows="10" :filters="filters" paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
            :rowsPerPageOptions="[5,10,25]" currentPageReportTemplate="Showing {first} to {last} of {totalRecords} products" class="p-datatable-striped">

                <template #header>
                    <div class="table-header p-d-flex p-jc-between p-ai-center">
                        <div>
                        <Button label="Create Organisation" icon="pi pi-plus" class="p-button-success p-mr-2" @click="openCreateOrganisationDialog" />
                        <Button label="Invite Organisation(s)" icon="pi pi-plus" class="p-button-success p-mr-2" @click="something" disabled="disabled" />
                        </div>
                        <div>
                        <span class="p-input-icon-left">
                            <i class="pi pi-search" />
                            <InputText v-model="filters['global']" placeholder="Search..." />
                        </span>
                        </div>
                    </div>
                </template>

                <Column field="ispublic" header="Public" :sortable="true"></Column>
                <Column field="name" header="Name" :sortable="true"></Column>
                <Column field="description" header="Description" :sortable="true"></Column>
                <Column field="participants.length" header="Participants" :sortable="true"></Column>
                <Column field="creator.username" header="Created by" :sortable="true"></Column> creator instead of created_by attribute!
            </DataTable> -->
    <div class="organisations">
        <h1>Organisations Overview</h1>
        <Toast position="top-right"/>
        <div class="card p-m-5 p-shadow-2">
            <Toolbar>
                <template #left>
                        <ToggleButton v-model="selectionToggle" onLabel="Selecting: Enabled" offLabel="Selecting: Disabled" onIcon="pi pi-check" offIcon="pi pi-times" />
                        <Button label="Create Organisation" icon="pi pi-plus" class="p-button-success p-mx-2" @click="openCreateOrganisationDialog" />
                        <Button label="Invite Organisation(s)" icon="pi pi-plus" class="p-button-success" @click="something" disabled="disabled" />
                </template>
                <template #right>
                    <span class="p-input-icon-left">
                        <i class="pi pi-search" />
                        <InputText v-model="filters['global']" placeholder="Search..." />
                    </span>
                </template>
            </Toolbar>
            <personalised-datatable table-name="organisations" selectionToggle :columns="OrganisationsColumns" :filters="filters"
            :custom-data="organisations" @item-redirect="goToOrganisation"/>
        </div>
    </div>

    <Dialog v-model:visible="organisationDialog" :style="{width: '450px'}" header="Organisation Details" :modal="true" class="p-fluid">
        <div class="p-field">
            <label for="name">Name</label>
            <InputText id="name" v-model.trim="organisation.name" required="true" autofocus :class="{'p-invalid': submitted && !organisation.name}"
            @blur="updateOrganisationForm({ name: $event.target.value })" />
            <small class="p-error" v-if="submitted && !organisation.name">Name is required.</small>
        </div>
        <div class="p-field">
            <label for="description">Description</label>
            <Textarea id="description" v-model="organisation.description" required="true" rows="3" cols="20"
            @blur="updateOrganisationForm({ description: $event.target.value })" />
        </div>
        <div class="p-field">
            <label for="ispublic">Should this organisation be public? </label>
            <SelectButton id="ispublic" v-model="boolChoice" required="true" :options="ispublicbool"
            @blur="updateOrganisationForm({ ispublic: boolChoice })" />
        </div>
        <template #footer>
            <Button label="Cancel" icon="pi pi-times" class="p-button-text" @click="hideDialog"/>
            <Button label="Save" icon="pi pi-check" class="p-button-text" @click="saveOrganisation" :disabled="!organisation.name" />
        </template>
    </Dialog>

    <Dialog v-model:visible="deleteOrganisationDialog" :style="{width: '450px'}" header="Confirm" :modal="true">
        <div class="confirmation-content">
            <i class="pi pi-exclamation-triangle p-mr-3" style="font-size: 2rem" />
            <span v-if="organisation">Are you sure you want to delete <b>{{organisation.name}}</b>?</span>
        </div>
        <template #footer>
            <Button label="No" icon="pi pi-times" class="p-button-text" @click="deleteOrganisationDialog = false"/>
            <Button label="Yes" icon="pi pi-check" class="p-button-text" @click="removeOrganisation(organisation)" />
        </template>
    </Dialog>

    <Dialog v-model:visible="deleteOrganisationsDialog" :style="{width: '450px'}" header="Confirm" :modal="true">
        <div class="confirmation-content">
            <i class="pi pi-exclamation-triangle p-mr-3" style="font-size: 2rem" />
            <span v-if="organisation">Are you sure you want to delete the selected products?</span>
        </div>
        <template #footer>
            <Button label="No" icon="pi pi-times" class="p-button-text" @click="deleteOrganisationsDialog = false"/>
            <Button label="Yes" icon="pi pi-check" class="p-button-text" @click="deleteSelectedOrganisations" />
        </template>
    </Dialog>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import PersonalisedDatatable from '../components/PersonalisedDatatable'
// import { useToast } from 'primevue/usetoast'

export default {
    components: {
        PersonalisedDatatable
    },
     setup () {
         // const toast = useToast()
        const succesmessage = () => {
             this.$toast.add(({ severity: 'success', summary: 'Successful', detail: 'Message Content', life: 3000 }))
         }
         return {
             succesmessage
         }
     },
    data () {
        return {
            OrganisationsColumns: [
                { field: 'ispublic', header: 'Public' },
                { field: 'name', header: 'Name' },
                { field: 'description', header: 'Description' },
                { field: 'participants.length', header: 'Participants' },
                { field: 'creator.username', header: 'Created by' }
            ],
            selectionToggle: false,
            selectedOrganisations: null,
            filters: {},
            ispublicbool: [true, false],
            boolChoice: null,
            organisationDialog: false,
            submitted: false
        }
    },
    computed: {
        ...mapState('organisation', ['organisations', 'organisation'])
    },
    created () {
        this.initialize()
    },
    methods: {
        ...mapActions('organisation', ['fetchOrganisations', 'setOrganisation', 'createOrganisation', 'updateOrganisationForm']),
        async initialize () {
            await this.fetchOrganisations({})
        },
        async openCreateOrganisationDialog () {
            this.setOrganisation({})
            this.submitted = false
            this.organisationDialog = true
        },
        saveOrganisation () {
            this.submitted = true
            if (this.organisation.name.trim()) {
                this.createOrganisation({})
                this.$toast.add({ severity: 'success', summary: 'Successful', detail: 'Organisation Created', life: 3000 })
            this.organisationDialog = false
            this.$router.push({ name: 'organisationdetails', params: { id: this.organisation.id } })
            }
        },
        hideDialog () {
            this.organisationDialog = false
            this.submitted = true
         },

        goToOrganisation (selectedRows) {
            if (!this.selectionToggle) {
                this.setOrganisation({ ...selectedRows[0] })
                // this.$toast.add({ severity: 'info', summary: 'Network Selected', detail: 'Name: ' + event.name, life: 3000 })
                this.$router.push({ name: 'organisationdetails', params: { id: this.organisation.id } })
            } else {
                this.selectedOrganisations = selectedRows
            }
        }
    }
}
        //  findIndexById (id) {
        //      let index = -1
        //      for (let i = 0; i < this.$store.state.organisations.length; i++) {
        //          if (this.$store.state.organisations[i].id === id) {
        //              index = i
        //              break
        //          }
        //      }
        //      return index
        // },

        // async removeOrganisation (organisation) {
        //     this.deleteOrganisationDialog = false
        //     this.deleteOrganisation({ id: organisation.id })
        //     // this.organisation = {}
        //     this.$toast.add({ severity: 'success', summary: 'Successful', detail: 'Organisation Deleted', life: 3000 })
        // },
        //   confirmDeleteSelected () {
        //       this.deleteOrganisationsDialog = true
        //   },
        //  confirmDeleteOrganisation (organisation) {
        //      this.organisation = organisation
        //      this.deleteOrganisationDialog = true
        //  },
        //  editOrganisation (organisation) {
        //      this.organisation = { ...organisation }
        //      this.organisationDialog = true
        //  },
        // deleteSelectedOrganisations () {
        //     this.$store.state.organisations = this.$store.state.organisations.filter(val => !this.selectedOrganisations.includes(val))
        //     this.deleteOrganisationsDialog = false
        //     this.selectedOrganisations = null
        //     this.$toast.add({ severity: 'success', summary: 'Successful', detail: 'Organisations removed', life: 3000 })
        // },
        //  deleteOrganisation () {
        //      this.$store.state.organisations = this.$store.state.organisations.filter(val => val.id !== this.organisation.id)
        //      this.organisation = {}
        //      this.$toast.add({ severity: 'success', summary: 'Successful', detail: 'Organisation Deleted', life: 3000 })
        //  },

                // if (this.organisation.id) {
                //      this.$store.state.organisations[this.findIndexById(this.organisation.id)] = this.organisation

                //  } else {
        // AxiosInstance.get('/organisations/', { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
        //   .then(response => {
        //     this.$store.state.organisations = response.data
        //   })
        //   .catch(err => {
        //     console.log(err)
        //   })
</script>
