<template>
    <div class="users">
        <h1>Manage Users</h1>
        <Toast position="top-right"/>
        <div class="card p-m-5 p-shadow-2">
              <Toolbar>
                <template #left>
                    <ToggleButton v-model="selectionToggle" onLabel="Selecting: Enabled" offLabel="Selecting: Disabled" onIcon="pi pi-check" offIcon="pi pi-times" class="p-mr-2" />
                    <Button label="Send Message" icon="pi pi-plus" class="p-button-success p-mr-2" @click="something" :disabled="selectedUsers.length === 0" />
                </template>

                <template #right>
                    <span class="p-input-icon-left">
                        <i class="pi pi-search" />
                        <InputText v-model="filters['global']" placeholder="Search..." />
                    </span>
                </template>
            </Toolbar>
          <personalised-datatable table-name="users" selectionToggle :columns="ParticipantsColumns" :filters="filters" :custom-data="users" @item-redirect="goToUser"/>

        </div>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import PersonalisedDatatable from '../../components/PersonalisedDatatable'

export default {
    name: 'Users',
    components: {
      PersonalisedDatatable
    },
    data () {
        return {
            ParticipantsColumns: [
                 { field: 'username', header: 'Username' },
                 { field: 'email', header: 'E-mail' },
                 { field: 'first_name', header: 'First Name' },
                 { field: 'last_name_prefix', header: 'Prefix' },
                 { field: 'last_name', header: 'Last Name' }
                 ],
            selectionToggle: false,
          filters: {},
          selectedUsers: []
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
        await this.fetchUsers({})
      },
      goToUser (selectedRows) {
        console.log(selectedRows)
        this.$toast.add({ severity: 'info', summary: 'User Selected', detail: `${selectedRows[selectedRows.length - 1].username}`, life: 3000 })
        if (!this.selectionToggle) {
          this.setUser({ ...selectedRows[0] })
          this.$router.push({ name: 'userdetails', params: { id: this.user.id } })
        } else {
          this.selectedUsers = selectedRows
          console.log(this.selectedUsers.length)
        }
      }
    }
}
        // AxiosInstance.get('/users/', { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
        // .then(response => {
        //     this.$store.state.users = response.data
        // })
        // .catch(err => {
        //     console.log(err)
        // })
</script>
