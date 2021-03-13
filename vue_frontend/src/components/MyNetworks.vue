<template>
   <Toolbar>
        <template #left>
            <!-- <ToggleButton v-if="selectionEnabled" v-model="selectionToggle" onLabel="Selecting: Enabled" offLabel="Selecting: Disabled" onIcon="pi pi-check" offIcon="pi pi-times" class="p-mr-2" /> -->
            <div v-if="!organisationnetworks">
                 <Button label="Create Network" icon="pi pi-plus" class="p-button-success p-mr-2" @click="createDialog = true" />
                <Button label="Delete Network" icon="pi pi-trash" class="p-button-danger" @click="confirmationDialog = true" :disabled="!selectedRows.length" />
            </div>
        </template>
        <template #right>
            <span class="p-input-icon-left">
                <i class="pi pi-search" />
                <InputText v-model="filters['global']" placeholder="Search..." />
            </span>
        </template>
    </Toolbar>
<div v-if="networks.length">
        <DataTable ref="dt" :value="networks" v-model:selection="selectedRows" :selectionMode="selectionToggle? 'multiple' : 'single'" dataKey="id" :metaKeySelection="false" @row-select="goToSelectedNetwork"
        :paginator="true" :rows="10" :filters="filters" paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
        :rowsPerPageOptions="[5,10,25]" currentPageReportTemplate="Showing {first} to {last} of {totalRecords} products" class="p-datatable-striped">

        <Column v-for="col of columns" :field="col.field" :header="col.header" :key="col.field" />
        </Datatable>
    </div>
    <div v-else class="p-p-3"><h3 class="p-text-light p-text-italic">There are no networks to display</h3></div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
    props: {
        columns: {
            type: Array,
            default: function () {
                return [
                    { field: 'ispublic', header: 'Public' },
                    { field: 'name', header: 'Name' },
                    { field: 'description', header: 'Description' },
                    { field: 'organisations.length', header: 'Organisations' },
                    { field: 'created_by.username', header: 'Created by' }
                ]
            }
        },
        organisationnetworks: {
            type: Boolean,
            default: false
        },
        query: {
            type: String,
            default: ''
        },
        selectionEnabled: {
            type: Boolean,
            default: false
        }
    },
    data () {
        return {
            filters: {},
            selectedRows: [],
            selectionToggle: false
        }
    },
    computed: {
        ...mapState('network', ['networks', 'network'])
    },
    created () {
        this.initialize()
    },
    methods: {
        ...mapActions('network', ['fetchNetworks', 'setNetwork']),
        async initialize () {
            await this.fetchNetworks({ query: this.query })
        },
        async goToSelectedNetwork (event) {
            await this.setNetwork(event.data)
            this.$router.push({ name: 'networkdetails', params: { id: this.network?.id || 0 } })
        }
    }
}
</script>
