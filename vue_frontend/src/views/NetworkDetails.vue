<template>
    <div class="card p-mx-5">
          <h1>{{ network.name }} - created by {{ network.created_by }}</h1>
        <div class="p-grid">
            <div class="p-col-5 p-d-flex p-ai-center p-jc-center">
                <div class="p-fluid">
                   <p class="p-text-justify">{{ network.description }} - Lorem ipsum dolor sit amet, consectetur adipiscing elit. In convallis mi sit amet faucibus malesuada. Vestibulum fringilla sed dui bibendum laoreet. Donec suscipit sit amet leo et mattis. Aenean mattis tempus turpis a vulputate. Nunc bibendum pulvinar neque, nec mattis nisl tincidunt ut. Nam a quam id justo dictum pulvinar. Sed luctus dictum ligula, id sagittis tellus aliquam id. Vestibulum auctor vestibulum turpis.</p>
                    </div>
            </div>
            <div class="p-col-2">
                <Divider layout="vertical">
                </Divider>
            </div>
            <div class="p-col-5 p-d-flex p-ai-center p-jc-center">
                 <p>{{ network.created_by }}</p>
                <Button label="Edit Network" icon="pi pi-user-plus" class="p-button-success p-mr-2"></Button>
                <Button label="Delete Network" icon="pi pi-trash" class="p-button-danger" @click="confirmDeletion" />
            </div>
        </div>
    </div>

    <div class="card p-m-5 p-shadow-2">
        <DataTable ref="dt" :value="networkorganisations" v-model:selection="selectedOrganisations" selectionMode="single" dataKey="id"
        :paginator="true" :rows="10" :filters="filters" paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
        :rowsPerPageOptions="[5,10,25]" currentPageReportTemplate="Showing {first} to {last} of {totalRecords} products" class="p-datatable-striped">

            <h1>Members</h1>
            <Toolbar>
                <template #left>
                    <Button label="Invite" icon="pi pi-plus" class="p-button-success p-mr-2" @click="nothingyet" />
                    <Button label="Remove" icon="pi pi-trash" class="p-button-danger" @click="nothingyet" :disabled="!selectedProducts || !selectedProducts.length" />
                </template>

                <template #right>
                    <span class="p-input-icon-left">
                        <i class="pi pi-search" />
                        <InputText v-model="filters['global']" placeholder="Search..." />
                    </span>
                </template>
            </Toolbar>

            <Column field="ispublic" header="Public" :sortable="true"></Column>
            <Column field="name" header="Name" :sortable="true"></Column>
            <Column field="description" header="Description" :sortable="true"></Column>
            <Column field="participants" header="Participants" :sortable="true"></Column>
            <Column field="creator" header="Created by" :sortable="true"></Column>
        </DataTable>
    </div>

    <Dialog v-model:visible="editNetworkDialog" :style="{width: '450px'}" header="Network Details" :modal="true" class="p-fluid">
        <div class="p-field">
            <label for="name">Name</label>
            <InputText id="name" v-model.trim="network.name" required="true" autofocus :class="{'p-invalid': submitted && !network.name}" />
            <small class="p-error" v-if="submitted && !network.name">Name is required.</small>
        </div>
        <div class="p-field">
            <label for="description">Description</label>
            <Textarea id="description" v-model="network.description" required="true" rows="3" cols="20" />
        </div>
        <div class="p-field">
            <label for="ispublic">Should this network be public? </label>
            <SelectButton id="ispublic" v-model="network.ispublic" :options="ispublicbool" />
        </div>
        <template #footer>
            <Button label="Cancel" icon="pi pi-times" class="p-button-text" @click="hideDialogs"/>
            <Button label="Save" icon="pi pi-check" class="p-button-text" @click="editNetwork" :disabled="!network.name" />
        </template>
    </Dialog>

    <Dialog v-model:visible="deleteNetworkDialog" :style="{width: '450px'}" header="Confirm" :modal="true">
      <div class="confirmation-content">
          <i class="pi pi-exclamation-triangle p-mr-3" style="font-size: 2rem" />
            <span v-if="network">Are you sure you want to delete <b>{{network.name}}</b>?</span>
      </div>
      <template #footer>
        <Button label="No" icon="pi pi-times" class="p-button-text" @click="deleteNetworkDialog = false"/>
        <Button label="Yes" icon="pi pi-check" class="p-button-text" @click="removeNetwork()" />
      </template>
    </Dialog>
</template>

<script>
// import { AxiosInstance } from '../plugins/axios'
import { mapState, mapActions } from 'vuex'

export default {
    data () {
        return {
            editNetworkDialog: false,
            deleteNetworkDialog: false,
            selectedOrganisations: null, // might be removable
            filters: {},
            submitted: false
        }
    },
    computed: {
        ...mapState('network', ['network', 'networkorganisations'])
    },
    created () {
        this.initialize()
    },
    methods: {
        ...mapActions('network', ['fetchNetwork', 'fetchNetworkOrganisations', 'updateNetwork', 'deleteNetwork']),
        async initialize () {
            await this.fetchNetwork({ id: this.network?.id || 0 })
            await this.fetchNetworkOrganisations(this.network?.id || 0)
        },
        async editNetwork () {
            this.editNetworkDialog = true
            await this.updateNetwork({})
            this.$toast.add({ severity: 'success', summary: 'Successful', detail: 'Network Updated', life: 3000 })
        },
        confirmDeletion () {
            this.deleteNetworkDialog = true
        },
        async removeNetwork () {
            this.deleteNetworkDialog = false
            await this.deleteNetwork({ id: this.network?.id || 0 })
            this.$toast.add({ severity: 'success', summary: 'Succesful', detail: 'Network Deleted', life: 3000 })
             this.$router.push({ name: 'networks' })
        },
        hideDialogs () {
            this.editNetworkDialog = false
            this.deleteNetworkDialog = false
        }
    }
}
</script>
