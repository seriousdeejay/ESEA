<template>
    <div>
        <h1>
        to do:
        -User column with organisations and Networks
        - firstname+prefix+lastname in 1 column
        - Remove Buttons
        </h1>
    </div>

    <div class="users">
        <h1>Manage Users</h1>
        <Toast position="top-right"/>
        <div class="card p-m-5 p-shadow-2">
            <DataTable ref="dt" :value="users" v-model:selection="selectedUsers" selectionMode="single" dataKey="id" @row-select="goToUser"
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

                <Column field="username" header="Username" :sortable="true"></Column>
                <Column field="email" header="Email" :sortable="true"></Column>
                <Column field="first_name" header="First name" :sortable="true"></Column>
                <Column field="last_name_prefix" header="Prefix" :sortable="true"></Column>
                <Column field="last_name" header="Last Name" :sortable="true"></Column>
                <Column :exportable="false">
                    <template #body="slotProps">
                        <Button icon="pi pi-pencil" class="p-button-rounded p-button-success p-mr-2" @click="editUser(slotProps.data)" :disabled=true />
                        <Button icon="pi pi-trash" class="p-button-rounded p-button-danger" @click="confirmDeleteUser(slotProps.data)" :disabled=true />
                    </template>
                </Column>
            </DataTable>
        </div>
    </div>

    <Dialog v-model:visible="userDialog" :style="{width: '450px'}" header="User Details" :modal="true" class="p-fluid">
        <div class="p-field">
            <label for="name">Name</label>
            <InputText id="name" v-model.trim="user.name" required="true" autofocus :class="{'p-invalid': submitted && !user.name}" />
            <small class="p-error" v-if="submitted && !user.name">Name is required.</small>
        </div>
        <div class="p-field">
            <label for="description">Description</label>
            <Textarea id="description" v-model="user.description" required="true" rows="3" cols="20" />
        </div>
        <div class="p-field">
            <label for="ispublic">Should this user be public? </label>
            <SelectButton id="ispublic" v-model="user.ispublic" :options="ispublicbool" />
        </div>
        <template #footer>
            <Button label="Cancel" icon="pi pi-times" class="p-button-text" @click="hideDialog"/>
            <Button label="Save" icon="pi pi-check" class="p-button-text" @click="saveUser" :disabled="!user.name" />
        </template>
    </Dialog>

    <Dialog v-model:visible="deleteUserDialog" :style="{width: '450px'}" header="Confirm" :modal="true">
      <div class="confirmation-content">
          <i class="pi pi-exclamation-triangle p-mr-3" style="font-size: 2rem" />
            <span v-if="user">Are you sure you want to delete <b>{{user.name}}</b>?</span>
      </div>
      <template #footer>
        <Button label="No" icon="pi pi-times" class="p-button-text" @click="deleteUserDialog = false"/>
        <Button label="Yes" icon="pi pi-check" class="p-button-text" @click="deleteUser" />
      </template>
    </Dialog>
</template>

<script>
import { AxiosInstance } from '../plugins/axios'
import { mapState } from 'vuex'

export default {
    name: 'Users',
    data () {
        return {
          deleteUserDialog: false,
          filters: {},
          ispublicbool: ['true', 'false'],
          user: {},
          userDialog: false,
          selectedUsers: null,
          submitted: false
        }
    },
    computed: mapState(['users']),
    created () {
        AxiosInstance.get('/users/', { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
        .then(response => {
            this.$store.state.users = response.data
        })
        .catch(err => {
            console.log(err)
        })
    },
    methods: {
      openNew () {
        this.user = {}
        this.submitted = false
        this.userDialog = true
      },
      editUser (user) {
        this.user = { ...user }
        this.userDialog = true
      },
      deleteUser () {
        this.deleteUserDialog = true
        this.users = this.users.filter(val => val.id !== this.user.id)
        this.user = {}
        this.$toast.add({ severity: 'success', summary: 'Succesful', detail: 'User Deleted', life: 3000 })
      },
      confirmDeleteUser (user) {
        this.user = user
        this.deleteUserDialog = true
      },
      saveUser (user) {
        this.submitted = true
        if (this.user.name.trim()) {
          if (this.user.id) {
            this.users[this.findIndexById(this.user.id)] = this.user
            this.$toast.add({ severity: 'success', summary: 'Succesful', detail: 'User updated', life: 3000 })
          } else {
            this.users.push(this.user)
            this.$toast.add({ severity: 'success', summary: 'Succesful', detail: 'User created', life: 3000 })
          }
        this.userDialog = false
        this.user = {}
        }
      },
      hideDialog () {
        this.userDialog = false
        this.submitted = true
      },
      findIndexById (id) {
          let index = -1
          for (let i = 0; i < this.users.length; i++) {
              if (this.users[i].id === id) {
                index = i
                  break
              }
          }

          return index
        },
        goToUser (user) {
          this.user = { ...user }
          this.$toast.add({ severity: 'info', summary: 'User Selected', detail: 'Name: ' + user.name, life: 3000 })
          this.$router.push({ name: 'users', params: { id: this.selectedUsers.id } })
        }
      }
}
</script>
