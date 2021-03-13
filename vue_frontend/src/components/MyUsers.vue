<template>
    <Toolbar>
        <template #left>
        <ToggleButton v-if="selectionEnabled" v-model="selectionToggle" onLabel="Selecting: Enabled" offLabel="Selecting: Disabled" onIcon="pi pi-check" offIcon="pi pi-times" class="p-mr-2" />
        <Button label="Invite users" icon="pi pi-plus" class="p-button-success p-mr-2" @click="addableOrganisations()" />
        <Button label="Remove members" icon="pi pi-trash" class="p-button-danger" @click="confirmationDialog = true" :disabled="!selectedRows.length" />
        </template>

        <template #right>
            <span class="p-input-icon-left">
                <i class="pi pi-search" />
                <InputText v-model="filters['global']" placeholder="Search..." />
            </span>
        </template>
    </Toolbar>
    <div v-if="users.length">
         <DataTable ref="dt" :value="users" v-model:selection="selectedRows" :selectionMode="selectionToggle? 'multiple' : 'single'" dataKey="id" :metaKeySelection="false" @row-select="goToSelectedUser"
        :paginator="true" :rows="10" :filters="filters" paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
        :rowsPerPageOptions="[5,10,25]" currentPageReportTemplate="Showing {first} to {last} of {totalRecords} products" class="p-datatable-striped">

        <Column v-for="col of columns" :field="col.field" :header="col.header" :key="col.field" />
        </Datatable>
    </div>
</template>
<script>
import { mapActions, mapState } from 'vuex'
export default {
    props: {
        columns: {
            type: Array,
            default: function () {
                return [
                    { field: 'username', header: 'Username' },
                    { field: 'first_name', header: 'First Name' },
                    { field: 'last_name_prefix', header: 'Prefix' },
                    { field: 'last_name', header: 'Last Name' }
                    // stakeholder group
                ]
            }
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
        ...mapState('user', ['users', 'user'])
    },
    created () {
        this.initialize()
    },
    methods: {
        ...mapActions('user', ['fetchUsers', 'setUser']),
        async initialize () {
            await this.fetchUsers({ })
            // query: `excludeorganisation=${this.$route.params.id || 0}`
        },
        async goToSelectedUser (event) {
            console.log(event.data)
            await this.setUser(event.data)
            this.$router.push({ name: 'userdetails', params: { id: this.user?.id || 0 } })
        }
    }
}
</script>
