<template>
    <div class="organisations">
        <h1>Manage Organisations</h1>
        <Toast position="top-right"/>
        <div class="card p-m-5 p-shadow-2">
            <DataTable ref="dt" :value="organisations" v-model:selection="selectedOrganisations" selectionMode="single" dataKey="id" @row-select="goToOrganisation"
            :paginator="true" :rows="10" :filters="filters" paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
            :rowsPerPageOptions="[5,10,25]" currentPageReportTemplate="Showing {first} to {last} of {totalRecords} products" class="p-datatable-striped">
                <template #header>
                    <div class="table-header p-d-flex p-jc-between p-ai-center">
                        <Button label="New" icon="pi pi-plus" class="p-button-success p-mr-2" @click="openNew" />
                        <span class="p-input-icon-left">
                            <i class="pi pi-search" />
                            <InputText v-model="filters['global']" placeholder="Search..." />
                        </span>
                    </div>
                </template>
                <Column field="ispublic" header="Public" :sortable="true"></Column>
                <Column field="name" header="Name" :sortable="true"></Column>
                <Column field="description" header="Description" :sortable="true"></Column>
                <Column field="participants.length" header="Participants" :sortable="true"></Column>
                <Column field="creator" header="Created by" :sortable="true"></Column>
                <Column :exportable="false">
                    <template #body="slotProps">
                        <Button icon="pi pi-pencil" class="p-button-rounded p-button-success p-mr-2" @click="editOrganisation(slotProps.data)" />
                        <Button icon="pi pi-trash" class="p-button-rounded p-button-danger" @click="confirmDeleteOrganisation(slotProps.data)" />
                    </template>
                </Column>
            </DataTable>
        </div>
    </div>

    <Dialog v-model:visible="organisationDialog" :style="{width: '450px'}" header="Organisation Details" :modal="true" class="p-fluid">
        <div class="p-field">
            <label for="name">Name</label>
            <InputText id="name" v-model.trim="organisation.name" required="true" autofocus :class="{'p-invalid': submitted && !organisation.name}" />
            <small class="p-error" v-if="submitted && !organisation.name">Name is required.</small>
        </div>
        <div class="p-field">
            <label for="description">Description</label>
            <Textarea id="description" v-model="organisation.description" required="true" rows="3" cols="20" />
        </div>
        <div class="p-field">
            <label for="ispublic">Should this organisation be public? </label>
            <SelectButton id="ispublic" v-model="organisation.ispublic" :options="ispublicbool" />
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
// import { AxiosInstance } from '../plugins/axios'
import { mapState, mapActions } from 'vuex'
import { useToast } from 'primevue/usetoast'

export default {
     setup () {
         const toast = useToast()

         const succesmessage = () => {
             toast.add(({ severity: 'success', summary: 'Successful', detail: 'Message Content', life: 3000 }))
         }
         return {
             succesmessage
         }
     },
    data () {
        return {
            selectedOrganisations: null,
            // organisation: {},
            ispublicbool: ['true', 'false'
            ],
            organisationDialog: false,
            deleteOrganisationDialog: false,
             deleteOrganisationsDialog: false,
            filters: {},
            submitted: false
        }
    },
    computed: {
        ...mapState('organisation', ['organisations'])
    },
    created () {
        this.initialize()
        // AxiosInstance.get('/organisations/', { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
        //   .then(response => {
        //     this.$store.state.organisations = response.data
        //   })
        //   .catch(err => {
        //     console.log(err)
        //   })
    },
    methods: {
        ...mapActions('organisation', ['fetchOrganisations', 'deleteOrganisation']),
        async initialize () {
            await this.fetchOrganisations({})
        },
        async removeOrganisation (organisation) {
            this.deleteOrganisationDialog = false
            this.deleteOrganisation({ id: organisation.id })
            // this.organisation = {}
            this.$toast.add({ severity: 'success', summary: 'Successful', detail: 'Organisation Deleted', life: 3000 })
        },
         openNew () {
             this.organisation = {}
             this.submitted = false
             this.organisationDialog = true
         },
          confirmDeleteSelected () {
              this.deleteOrganisationsDialog = true
          },
         confirmDeleteOrganisation (organisation) {
             this.organisation = organisation
             this.deleteOrganisationDialog = true
         },
         editOrganisation (organisation) {
             this.organisation = { ...organisation }
             this.organisationDialog = true
         },
          deleteSelectedOrganisations () {
              this.$store.state.organisations = this.$store.state.organisations.filter(val => !this.selectedOrganisations.includes(val))
              this.deleteOrganisationsDialog = false
              this.selectedOrganisations = null
              this.$toast.add({ severity: 'success', summary: 'Successful', detail: 'Organisations removed', life: 3000 })
          },
        //  deleteOrganisation () {
        //      this.$store.state.organisations = this.$store.state.organisations.filter(val => val.id !== this.organisation.id)
        //      this.organisation = {}
        //      this.$toast.add({ severity: 'success', summary: 'Successful', detail: 'Organisation Deleted', life: 3000 })
        //  },
         hideDialog () {
             this.organisationDialog = false
             this.submitted = true
         },
         saveOrganisation (organisation) {
             this.submitted = true
             if (this.organisation.name.trim()) {
                 if (this.organisation.id) {
                     this.$store.state.organisations[this.findIndexById(this.organisation.id)] = this.organisation
                     this.$toast.add({ severity: 'success', summary: 'Successful', detail: 'Organisation Updated', life: 3000 })
                 } else {
                 this.$store.state.organisations.push(this.organisation)
                 this.$toast.add({ severity: 'success', summary: 'Successful', detail: 'Organisation Created', life: 3000 })
                 }
             this.organisationDialog = false
             this.organisation = {}
             }
         },
         findIndexById (id) {
             let index = -1
             for (let i = 0; i < this.$store.state.organisations.length; i++) {
                 if (this.$store.state.organisations[i].id === id) {
                     index = i
                     break
                 }
             }
             return index
        },
        goToOrganisation (organisation) {
            this.organisation = { ...organisation }
            this.$toast.add({ severity: 'info', summary: 'Organisation Selected', detail: 'Name: ' + organisation.name, life: 3000 })
            this.$router.push({ name: 'organisationdetails', params: { id: this.selectedOrganisations.id } })
        }
    }
}
</script>
