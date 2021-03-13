<template>
    <Toolbar>
        <template #left>
        <ToggleButton v-if="selectionEnabled" v-model="selectionToggle" onLabel="Selecting: Enabled" offLabel="Selecting: Disabled" onIcon="pi pi-check" offIcon="pi pi-times" class="p-mr-2" />
            <div v-if="!addingProcess">
            <Button label="Invite users" icon="pi pi-plus" class="p-button-success p-mr-2" @click="addableUsers()" />
            <Button label="Remove members" icon="pi pi-trash" class="p-button-danger" @click="Dialog = true" :disabled="!selectedRows.length" />
            </div>
            <div v-else>
                <Button label="Show members" class="p-button-secondary p-mr-2" @click="initialize()" />
                <Button label="Invite selected Users" icon="pi pi-plus" class="p-button-success p-mr-2" @click="Dialog=true" :disabled="!selectedRows.length"/>
            </div>
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

<Dialog v-model:visible="Dialog" :style="{width: '450px'}" header="Confirm" :modal="true">
        <div class="confirmation-content">
            <i class="pi pi-exclamation-triangle p-mr-3" style="font-size: 2rem" />
            <span>Are you sure you want to {{addingProcess? 'join': 'delete'}}: </span>
                <div v-for="user in selectedRows" :key="user.id">
                    <b>{{user.username}} </b>
                    </div>
        </div>?
        <template #footer>
            <Button label="No" icon="pi pi-times" class="p-button-text" @click="Dialog = false"/>
            <Button label="Yes" icon="pi pi-check" class="p-button-text" @click="addOrRemoveUsers()" />
      </template>
    </Dialog>
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
            selectionToggle: false,
            addingProcess: false,
            Dialog: false
        }
    },
    computed: {
        ...mapState('user', ['users', 'user']),
        ...mapState('organisation', ['organisation'])
    },
    created () {
        this.initialize()
    },
    methods: {
        ...mapActions('user', ['fetchUsers', 'setUser']),
        ...mapActions('organisation', ['patchOrganisation']),
        async initialize () {
            await this.fetchUsers({ query: this.query })
            this.selectedRows = []
            this.addingProcess = false
            // query: `excludeorganisation=${this.$route.params.id || 0}`
        },
        async addableUsers () {
            console.log('>>', this.$route.params.OrganisationId)
            await this.fetchUsers({ query: '?excludeorganisation=3' })
            this.addingProcess = true
            this.selectionToggle = true
            this.selectedRows = []
        },
        async addOrRemoveUsers () {
            await this.patchOrganisation({ id: this.organisation.id, data: this.selectedRows })
            this.Dialog = false
            this.initialize()
        },
        async goToSelectedUser (event) {
            if (!this.selectionToggle) {
                await this.setUser(event.data)
                this.$router.push({ name: 'userdetails', params: { id: this.user?.id || 0 } })
            }
        }
    }
}
</script>
