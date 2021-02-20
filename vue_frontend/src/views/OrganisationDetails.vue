<template>
    <div class="card p-mx-5">
        <h1>{{ organisation.name }} - created by {{ organisation.creator }}</h1>
        <div class="p-grid">
            <div class="p-col-5 p-d-flex p-ai-center p-jc-center">
                <div class="p-fluid">
                   <p class="p-text-justify">{{ organisation.description }} - Lorem ipsum dolor sit amet, consectetur adipiscing elit. In convallis mi sit amet faucibus malesuada. Vestibulum fringilla sed dui bibendum laoreet. Donec suscipit sit amet leo et mattis. Aenean mattis tempus turpis a vulputate. Nunc bibendum pulvinar neque, nec mattis nisl tincidunt ut. Nam a quam id justo dictum pulvinar. Sed luctus dictum ligula, id sagittis tellus aliquam id. Vestibulum auctor vestibulum turpis.</p>
                    </div>
            </div>
            <div class="p-col-2">
                <Divider layout="vertical">
                </Divider>
            </div>
            <div class="p-col-5 p-d-flex p-ai-center p-jc-center">
                 <p>{{ organisation.creator }}</p>
                <Button label="Edit Organisation" icon="pi pi-user-plus" class="p-button-success p-mr-2" @click="editOrganisationDialog = true"/>
                <Button label="Delete Organisation" icon="pi pi-trash" class="p-button-danger" @click="confirmDeletion" />
            </div>
        </div>
    </div>

    <div class="card p-m-5 p-shadow-2">
        <DataTable ref="dt" :value="organisationparticipants" v-model:selection="selectedOrganisations" selectionMode="single" dataKey="id"
        :paginator="true" :rows="10" :filters="filters" paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
        :rowsPerPageOptions="[5,10,25]" currentPageReportTemplate="Showing {first} to {last} of {totalRecords} products" class="p-datatable-striped">

            <h1>Participants</h1>
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

            <Column field="username" header="Username" :sortable="true"></Column>
            <Column field="first_name" header="First name" :sortable="true"></Column> <!-- Should insert full name here! -->
        </DataTable>
    </div>

    <Dialog v-model:visible="editOrganisationDialog" :style="{width: '450px'}" header="Network Details" :modal="true" class="p-fluid">
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
            <Button label="Cancel" icon="pi pi-times" class="p-button-text" @click="hideDialogs"/>
            <Button label="Save" icon="pi pi-check" class="p-button-text" @click="editOrganisation" :disabled="!organisation.name" />
        </template>
    </Dialog>

    <Dialog v-model:visible="deleteOrganisationDialog" :style="{width: '450px'}" header="Confirm" :modal="true">
        <div class="confirmation-content">
            <i class="pi pi-exclamation-triangle p-mr-3" style="font-size: 2rem" />
            <span v-if="organisation">Are you sure you want to delete <b>{{organisation.name}}</b>?</span>
        </div>
        <template #footer>
            <Button label="No" icon="pi pi-times" class="p-button-text" @click="deleteOrganisationDialog = false"/>
            <Button label="Yes" icon="pi pi-check" class="p-button-text" @click="removeOrganisation()" />
        </template>
    </Dialog>
</template>

<script>
import { mapState, mapActions } from 'vuex'
// import { AxiosInstance } from '../plugins/axios'
// import { required, minLength } from 'vuelidate/lib/validators'

export default {
    data () {
        return {
            editOrganisationDialog: false,
            deleteOrganisationDialog: false,
            selectedOrganisations: null,
            filters: {},
            submitted: false
        }
    },
    computed: {
        ...mapState('organisation', ['organisation']) // organisationparticipants
    },
    created () {
        this.initialize()
    //     AxiosInstance.get(`/organisations/${this.$route.params.id}/`, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
    //       .then(response => { this.$store.state.organisation = response.data })
    //       .catch(err => { console.log(err) })
    //     AxiosInstance.get(`/organisationparticipants/${this.$route.params.id}/`, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
    //     .then(response => { this.$store.state.organisationparticipants = response.data })
    //     .catch(err => { console.log(err) })
    },
    methods: {
        ...mapActions('organisation', ['fetchOrganisation', 'updateOrganisation', 'deleteOrganisation']),
        async initialize () {
            console.log(this.organisation)
            await this.fetchOrganisation({ id: this.organisation?.id || 0 })
            console.log(this.organisation)
            // await this.fetchOrganisationParticipants(this.organisation?.id || 0)
        },
        async editOrganisation () {
            this.editOrganisationDialog = false
            await this.updateOrganisation({})
            this.$toast.add({ severity: 'success', summary: 'Successful', detail: 'Organisation Updated', life: 3000 })
        },
        confirmDeletion () {
            this.deleteOrganisationDialog = true
        },
        async removeOrganisation () {
            this.deleteOrganisationDialog = false
            await this.deleteOrganisation({ id: this.organisation?.id || 0 })
            this.$toast.add({ severity: 'success', summary: 'Succesful', detail: 'Organisation Deleted', life: 3000 })
            this.$router.push({ name: 'organisations' })
        },
        hideDialogs () {
            this.editOrganisation = false
            this.deleteOrganisation = false
        }
    }
}
</script>
