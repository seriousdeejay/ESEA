<template>
    <div class="networks">
        <h1>Networks</h1>
        <div class="card p-px-5">
            <Toolbar class="p-mb-4">
                <template #left>
                    <Button label="New" icon="pi pi-plus" class="p-button-success p-mr-2" @click="openNew" />
                    <Button label="Delete" icon="pi pi-trash" class="p-button-danger" @click="confirmDeleteSelected" :disabled="!selectedOrganisations || !selectedOrganisations.length" />
                </template>
                <template #right>
                    <FileUpload mode="basic" accept="image/*" :maxFileSize="1000000" label="Import" chooseLabel="Import" class="p-mr-2 p-d-inline-block" />
                    <Button label="Export" icon="pi pi-upload" class="p-button-help"   /> <!-- @click="exportCSV($event)" -->
                </template>
            </Toolbar>
            <DataTable ref="dt" :value="organisations" v-model:selection="selectedOrganisations" dataKey="id" :paginator="true" :rows="10" :filters="filters"
        paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown" :rowsPerPageOptions="[5,10,25]"
        currentPageReportTemplate="Showing {first} to {last} of {totalRecords} products">
                <template #header>
                    <div class="table-header p-d-flex p-jc-between p-ai-center">
                        <h2 class="p-m-0">Manage Organisations</h2>
                        <span class="p-input-icon-left">
                            <i class="pi pi-search" />
                            <InputText v-model="filters['global']" placeholder="Search..." />
                        </span>
                    </div>
                </template>
                <Column selectionMode="multiple" headerStyle="width: 3rem" :exportable="false"></Column>
                <Column field="name" header="Name" :sortable="true"></Column>
                <Column field="description" header="Description" :sortable="true"></Column>
                <Column field="creator" header="Creator" :sortable="true"></Column>
                <Column field="category" header="Category" :sortable="true"></Column>
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
                <Button label="Yes" icon="pi pi-check" class="p-button-text" @click="deleteOrganisation" />
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
export default {
    data () {
        return {
            selectedOrganisations: null,
            organisation: {},
            organisationDialog: false,
            deleteOrganisationDialog: false,
            deleteOrganisationsDialog: false,
            filters: {},
            submitted: false,
            organisations: [
                {
                    id: 1,
                    name: 'Organisation 3',
                    description: 'Des',
                    creator: 1,
                    participants: [],
                    title: 'gg',
                    content: 'ddd'
                },
                {
                    id: 2,
                    name: 'Organisation 2',
                    description: 'Description of Organisation 2',
                    creator: 1,
                    participants: [],
                    title: 'jj',
                    content: 'jj'
                }
            ]
        }
    },
    methods: {
        openNew () {
            this.organisation = {}
            this.submitted = false
            this.organisationDialog = true
        },
        confirmDeleteSelected () {
            this.deleteOrganisationsDialog = false
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
            this.organisation = this.organisations.filter(val => !this.selectedorganisations.includes(val))
            this.deleteOrganisationsDialog = false
            this.selectedOrganisations = null
            this.$toast.add({ severity: 'success', summary: 'Successful', detail: 'Organisations Deleted', life: 3000 })
        },
        hideDialog () {
            this.organisationDialog = false
            this.submitted = true
        },
        saveOrganisation () {
            this.submitted = true
            this.organisations.push(this.organisation)
            this.$toast.add({ severity: 'success', summary: 'Successful', detail: 'Organisation Created', life: 3000 })
        },
        pushed () {
        }
    }
}
</script>
