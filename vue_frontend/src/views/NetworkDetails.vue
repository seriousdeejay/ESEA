<template>
    <h1>{{ network.name }}</h1>
    <div class="card p-m-5 p-shadow-2">
    <!-- <Toolbar class="p-mb-4">
        <template #left>
            <Button label="New" icon="pi pi-plus" class="p-button-success p-mr-2" @click="openNew" />
            <Button label="Delete" icon="pi pi-trash" class="p-button-danger" @click="confirmDeleteSelected" :disabled="!selectedOrganisations || !selectedOrganisations.length" />
        </template>
        </Toolbar> -->
        <DataTable ref="dt" :value="networkorganisations" v-model:selection="selectedOrganisations" selectionMode="single" dataKey="id"
        :paginator="true" :rows="10" :filters="filters" paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
        :rowsPerPageOptions="[5,10,25]" currentPageReportTemplate="Showing {first} to {last} of {totalRecords} products" class="p-datatable-striped">
            <template #header>
                <div class="table-header p-d-flex p-jc-between p-ai-center">
                    <Button label="New" icon="pi pi-plus" class="p-button-success p-mr-2" @click="openNew" :disabled=true />
                    <span class="p-input-icon-left">
                        <i class="pi pi-search" />
                        <InputText v-model="filters['global']" placeholder="Search..." />
                    </span>
                </div>
            </template>
            <Column field="ispublic" header="Public" :sortable="true"></Column>
            <Column field="name" header="Name" :sortable="true"></Column>
            <Column field="description" header="Description" :sortable="true"></Column>
            <Column field="organisations" header="Organisations" :sortable="true"></Column>
            <Column field="created_by" header="Created by" :sortable="true"></Column>

            <!-- <template #body="slotProps">
                <Button icon="pi pi-pencil" class="p-button-rounded p-button-success p-mr-2" @click="editOrganisation(slotProps.data)" />
                <Button icon="pi pi-trash" class="p-button-rounded p-button-danger" @click="confirmDeleteOrganisation(slotProps.data)" />
            </template>
            </Column> -->
        </DataTable>
    </div>
</template>

<script>
import { AxiosInstance } from '../plugins/axios'
import { mapState } from 'vuex'

export default {
    data () {
        return {
            selectedOrganisations: null,
            filters: {}
        }
    },
    methods: {
    },
    computed: mapState(['accessToken', 'currentuser', 'network', 'networkorganisations']),
    created () {
        AxiosInstance.get(`/networks/${this.$route.params.id}/`, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
          .then(response => { this.$store.state.network = response.data })
          .catch(err => { console.log(err) })
        AxiosInstance.get(`/networkorganisations/${this.$route.params.id}/`, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
        .then(response => { this.$store.state.networkorganisations = response.data })
        .catch(err => { console.log(err) })
    }
}
</script>
