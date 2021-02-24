<template>
    <div class="card p-mx-5">
        <h1>{{ network.name }} - created by {{ network.created_by.username }}</h1>
        <div class="p-grid">
            <div class="p-col-5 p-d-flex p-ai-center p-jc-center">
                <div class="p-fluid">
                   <p class="p-text-justify">{{ network.description }} <br> Below you can find a tab with the organisations, methods, surveys, users and reports that are linked to this specific network. </p>
                </div>
            </div>
            <div class="p-col-2">
                <Divider layout="vertical" />
            </div>
            <div class="p-col-5 p-d-flex p-ai-center p-jc-center">
                 <p>{{ network.created_by.username }}</p>
                <Button label="Edit Network" icon="pi pi-user-plus" class="p-button-success p-m-2" @click="editNetworkDialog = true" />
                <Button label="Delete Network" icon="pi pi-trash" class="p-button-danger" @click="confirmDeletion" />
            </div>
        </div>
    </div>
    <TabView>
        <TabPanel header="Organisations">
            <!-- <div v-if="inviteOrganisationsWindow" class="p-shadow-1 p-p-2">
                <h3>Organisations of {{network.name}}</h3>
            </div>
            <div v-else>
                <h3>Organisations that can be invited</h3>
            </div> -->
                <Toolbar>
                    <template #left>
                        <ToggleButton v-model="selectionToggle" onLabel="Selecting: Enabled" offLabel="Selecting: Disabled" onIcon="pi pi-check" offIcon="pi pi-times" />
                        <div v-if="!inviteOrganisationsWindow">
                            <Button label="Invite Organisations" icon="pi pi-plus" class="p-button-success p-mx-2" @click="openInviteOrganisationsWindow" />
                            <Button label="Remove" icon="pi pi-trash" class="p-button-danger" @click="removeOrganisation" :disabled="!selectedOrganisations" />
                        </div>
                        <div v-else>
                            <Button label="Show Network's organisations" class="p-button-primary p-mx-2" @click="inviteOrganisationsWindow = false"/>
                            <Button label="Send invitation to selected organisations" icon="pi pi-plus" class="p-button-success" @click="sendInvitationToOrganisations" />
                        </div>
                    </template>
                    <template #right>
                        <span class="p-input-icon-left">
                            <i class="pi pi-search" />
                            <InputText v-model="filters['global']" placeholder="Search..." />
                        </span>
                    </template>
                </Toolbar>
                <personalised-datatable table-name="organisation" selectionToggle :columns="OrganisationsColumns" :filters="filters" :custom-data="inviteOrganisationsWindow? organisations : networkorganisations" @item-redirect="goToSelectedOrganisations"/>
                <!-- <div class="p-grid p-m-3">
                    <div class="p-col-3" v-for="organisation in networkorganisations" :key="organisation.id">
                        <div class="p-shadow-1 p-p-4" @click="testclick(organisation)">
                            <h3>{{ organisation.name }}</h3>
                            <h6>Founded by {{ organisation.creator.username }}</h6>
                            <p>{{ organisation.description }}</p>
                            <Button icon="pi pi-times" label="Remove" class="p-button-warning" />
                        </div>
                    </div>
                </div> -->
            <!-- <div v-if="inviteOrganisationsWindow" class="p-shadow-1 p-p-2">
                <h3>Organisations that can be invited</h3>
                <Toolbar>
                    <template #left>
                        <ToggleButton v-model="selectionToggle" onLabel="Selecting: Enabled" offLabel="Selecting: Disabled" onIcon="pi pi-check" offIcon="pi pi-times" class="p-mr-2" />
                    </template>

                    <template #right>
                        <span class="p-input-icon-left">
                            <i class="pi pi-search" />
                            <InputText v-model="filters['global']" placeholder="Search..." />
                        </span>
                    </template>
                </Toolbar>
                <personalised-datatable table-name="organisation" selectionToggle :columns="OrganisationsColumns" :filters="filters" :custom-data="organisations" @item-redirect="goToSelected2"/>
                <Button label="Cancel invitation" icon="pi pi-times" class="p-button-primary p-m-2" @click="inviteOrganisationsWindow = false"/>
                <Button label="Send invitation to selected organisations" icon="pi pi-plus" class="p-button-success p-m-2" @click="sendInvitationToOrganisations" />
            </div> -->

        </TabPanel>
        <TabPanel header="Methods">
            Content II
        </TabPanel>
        <TabPanel header="Surveys">
            Content III
        </TabPanel>
        <TabPanel header="Users">
            <personalised-datatable table-name="Members" selectionToggle :columns="ParticipantsColumns" :custom-data="users" @item-redirect="goToSelectedUsers"/>
        </TabPanel>
    </TabView>

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
// import OrganisationsVue from './Organisations.vue'
import PersonalisedDatatable from '../components/PersonalisedDatatable'

export default {
    components: {
        PersonalisedDatatable
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
            ParticipantsColumns: [
                 { field: 'username', header: 'Username' },
                 { field: 'email', header: 'E-mail' },
                 { field: 'first_name', header: 'First Name' },
                 { field: 'last_name_prefix', header: 'Prefix' },
                 { field: 'last_name', header: 'Last Name' }
                 ],
            selectionToggle: false,
            editNetworkDialog: false,
            deleteNetworkDialog: false,
            selectedOrganisations: null, // might be removable,
            inviteOrganisationsWindow: false,
            filters: {},
            ispublicbool: ['true', 'false'],
            submitted: false
        }
    },
    computed: {
        ...mapState('network', ['network', 'networkorganisations']),
        ...mapState('organisation', ['organisations', 'organisation']),
        ...mapState('user', ['users', 'user'])
    },
    created () {
        this.initialize()
    },
    methods: {
        ...mapActions('network', ['fetchNetwork', 'updateNetwork', 'deleteNetwork', 'deleteNetworkOrganisations']),
        ...mapActions('organisation', ['setOrganisation', 'fetchOrganisations']),
        ...mapActions('user', ['fetchUsers', 'setUser']),
        async initialize () {
            this.inviteOrganisationsWindow = false
            await this.fetchNetwork({ id: this.network?.id || 0 })
            console.log(this.networkorganisations)
            await this.fetchUsers({ query: `network=${this.network?.id || 0}` })
        },
        async editNetwork () {
            this.editNetworkDialog = false
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
        async removeOrganisation () {
            await this.deleteNetworkOrganisations({ data: this.selectedOrganisations })
            this.selectedOrganisations = null
            this.initialize()
        },
        async openInviteOrganisationsWindow () {
            await this.fetchOrganisations({ query: `excludenetwork=${this.network?.id || 0}` })
            this.inviteOrganisationsWindow = true
        },
        async sendInvitationToOrganisations () {
            await this.deleteNetworkOrganisations({ data: this.selectedOrganisations })
            this.initialize()
        },
        hideDialogs () {
            this.editNetworkDialog = false
            this.deleteNetworkDialog = false
        },
    //      goToSelected (event) {
    //         console.log({ ...event.data })
    //         this.setOrganisation({ ...event.data })
    //         this.$toast.add({ severity: 'info', summary: 'Network Selected', detail: 'Name: ' + event.name, life: 3000 })
    //         this.$router.push({ name: 'organisationdetails', params: { id: this.organisation.id } })
    //    },
        goToSelectedOrganisations (selectedRows) {
            // this.$toast.add({ severity: 'info', summary: 'Item Selected', detail: 'Name:', life: 3000 })
            if (!this.selectionToggle) {
                this.setOrganisation({ ...selectedRows[0] })
                this.$router.push({ name: 'organisationdetails', params: { id: this.organisation.id } })
            } else {
                this.selectedOrganisations = selectedRows
            }
       },
       goToSelectedUsers (selectedRows) {
           console.log(selectedRows[0], selectedRows)
        this.setUser({ ...selectedRows[0] })
        this.$router.push({ name: 'userdetails', params: { id: this.user.id } })
       }
    }
}
</script>
