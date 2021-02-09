<template>
    <div class="networks">
        <h1>Manage Networks</h1>
        <Toast position="top-right"/>
        <div class="card p-m-5 p-shadow-2">
            <DataTable ref="dt" :value="networks" v-model:selection="selectedNetworks" selectionMode="single" dataKey="id" @row-select="goToNetwork"
            :paginator="true" :rows="10" :filters="filters" paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
            :rowsPerPageOptions="[5,10,25]" currentPageReportTemplate="Showing {first} to {last} of {totalRecords} products" class="p-datatable-striped">

                <template #header>
                    <div class="table-header p-d-flex p-jc-between p-ai-center">
                        <Button label="New" icon="pi pi-plus" class="p-button-success p-mr-2" @click="openNew" />
                        <span class="p-input-icon-left">
                            <i class="pi pi-search" />
                            <InputText v-model="filters['global']" placeholder="Search..." />
                        </span>
                    </div>
                </template>

                <Column field="ispublic" header="Public" :sortable="true"></Column>
                <Column field="name" header="Name" :sortable="true"></Column>
                <Column field="description" header="Description" :sortable="true"></Column>
                <Column field="creator" header="Creator" :sortable="true"></Column>
                <Column :exportable="false">
                    <template #body="slotProps">
                        <Button icon="pi pi-pencil" class="p-button-rounded p-button-success p-mr-2" @click="editNetwork(slotProps.data)" />
                        <Button icon="pi pi-trash" class="p-button-rounded p-button-danger" @click="confirmDeleteNetwork(slotProps.data)" />
                    </template>
                </Column>
            </DataTable>
        </div>
    </div>

    <Dialog v-model:visible="networkDialog" :style="{width: '450px'}" header="Network Details" :modal="true" class="p-fluid">
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
            <Button label="Cancel" icon="pi pi-times" class="p-button-text" @click="hideDialog"/>
            <Button label="Save" icon="pi pi-check" class="p-button-text" @click="saveNetwork" :disabled="!network.name" />
        </template>
    </Dialog>

    <Dialog v-model:visible="deleteNetworkDialog" :style="{width: '450px'}" header="Confirm" :modal="true">
      <div class="confirmation-content">
          <i class="pi pi-exclamation-triangle p-mr-3" style="font-size: 2rem" />
            <span v-if="network">Are you sure you want to delete <b>{{network.name}}</b>?</span>
      </div>
      <template #footer>
        <Button label="No" icon="pi pi-times" class="p-button-text" @click="deleteNetworkDialog = false"/>
        <Button label="Yes" icon="pi pi-check" class="p-button-text" @click="deleteNetwork" />
      </template>
    </Dialog>
</template>

<script>
import { AxiosInstance } from '../plugins/axios'
import { mapState } from 'vuex'

export default {
    name: 'Networks',
    data () {
        return {
          deleteNetworkDialog: false,
          filters: {},
          ispublicbool: ['true', 'false'],
          network: {},
          networkDialog: false,
          selectedNetworks: null,
          submitted: false
        }
    },
    components: {
    },
    computed: mapState(['networks']),
    created () {
        AxiosInstance.get('/networks/', { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
          .then(response => {
            this.$store.state.networks = response.data
          })
          .catch(err => {
            console.log(err)
          })
    },
    methods: {
      openNew () {
        this.network = {}
        this.submitted = false
        this.networkDialog = true
      },
      editNetwork (network) {
        this.network = { ...network }
        this.networkDialog = true
      },
      deleteNetwork () {
        this.deleteNetworkDialog = true
        this.networks = this.networks.filter(val => val.id !== this.network.id)
        this.network = {}
        this.$toast.add({ severity: 'success', summary: 'Succesful', detail: 'Network Deleted', life: 3000 })
      },
      confirmDeleteNetwork (network) {
        this.network = network
        this.deleteNetworkDialog = true
      },
      saveNetwork (network) {
        this.submitted = true
        if (this.network.name.trim()) {
          if (this.network.id) {
            this.networks[this.findIndexById(this.network.id)] = this.network
            this.$toast.add({ severity: 'success', summary: 'Succesful', detail: 'Network updated', life: 3000 })
          } else {
            this.networks.push(this.network)
            this.$toast.add({ severity: 'success', summary: 'Succesful', detail: 'Network created', life: 3000 })
          }
        this.networkDialog = false
        this.network = {}
        }
      },
      hideDialog () {
        this.networkDialog = false
        this.submitted = true
      },
      findIndexById (id) {
          let index = -1
          for (let i = 0; i < this.networks.length; i++) {
              if (this.networks[i].id === id) {
                index = i
                  break
              }
          }

          return index
        },
        goToNetwork (network) {
          this.network = { ...network }
          this.$toast.add({ severity: 'info', summary: 'Network Selected', detail: 'Name: ' + network.name, life: 3000 })
          this.$router.push({ name: 'users', params: { id: this.selectedNetworks.id } })
        }
      }
}
</script>
