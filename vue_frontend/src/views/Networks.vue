        <template>
    <h1>Networks Overview</h1>
    <div class="networks">
        <Toast position="top-right"/>
        <div class="card p-m-5 p-shadow-2">
          <Toolbar>
                <template #left>
                        <Button label="Create Network" icon="pi pi-plus" class="p-button-success p-mx-2" @click="openCreateNetworkDialog" />
                </template>
                <template #right>
                    <span class="p-input-icon-left">
                        <i class="pi pi-search" />
                        <InputText v-model="filters['global']" placeholder="Search..." />
                    </span>
                </template>
            </Toolbar>
            <personalised-datatable table-name="networks" selection-toggle :columns="NetworkColumns" :filters="filters"
            :custom-data="networks" @item-redirect="goToNetwork"/>
        </div>
    </div>

    <Dialog v-model:visible="networkDialog" :style="{width: '450px'}" header="Network Details" :modal="true" class="p-fluid">
        <div class="p-field">
            <label for="name">Name</label>
            <InputText id="name" v-model.trim="network.name" required="true" autofocus :class="{'p-invalid': submitted && !network.name}"
            @blur="updateNetworkForm({ name: $event.target.value })" />
            <small class="p-error" v-if="submitted && !network.name">Name is required.</small>
        </div>
        <div class="p-field">
            <label for="description">Description</label>
            <Textarea id="description" v-model="network.description" required="true" rows="3" cols="20"
            @blur="updateNetworkForm({ description: $event.target.value })" />
        </div>
        <div class="p-field">
            <label for="ispublic">Should this network be public? </label>
            <SelectButton id="ispublic" v-model="boolChoice" required="true" :options="ispublicbool"
            @blur="updateNetworkForm({ ispublic: boolChoice })" />
        </div>
        <template #footer>
            <Button label="Cancel" icon="pi pi-times" class="p-button-text" @click="hideDialog"/>
            <Button label="Save" icon="pi pi-check" class="p-button-text" @click="saveNetwork" :disabled="!network.name" />
        </template>
    </Dialog>

</template>

<script>
import { mapState, mapActions } from 'vuex'
import PersonalisedDatatable from '../components/PersonalisedDatatable'

export default {
        components: {
        PersonalisedDatatable
    },
    data () {
        return {
            NetworkColumns: [
                { field: 'ispublic', header: 'Public' },
                { field: 'name', header: 'Name' },
                { field: 'description', header: 'Description' },
                { field: 'organisations.length', header: 'Organisations' },
                { field: 'created_by.username', header: 'Created by' }
            ],
            selectionToggle: false,
            selectedNetworks: null,
            filters: {},
            ispublicbool: [true, false],
            boolChoice: null,
            networkDialog: false,
            submitted: false
        }
    },
    computed: {
        ...mapState('network', ['networks', 'network'])
    },
    created () {
        this.initialize()
    },
    methods: {
        ...mapActions('network', ['fetchNetworks', 'setNetwork', 'createNetwork', 'updateNetworkForm']),
        async initialize () {
            await this.fetchNetworks({})
        },
        async openCreateNetworkDialog () {
            this.setNetwork({})
            this.submitted = false
            this.networkDialog = true
        },
        async saveNetwork () {
            this.submitted = true
            if (this.network.name.trim()) {
                await this.createNetwork({})
                this.$toast.add({ severity: 'success', summary: 'Succesful', detail: 'Network created', life: 3000 })
            this.networkDialog = false
            this.$router.push({ name: 'networkdetails', params: { id: this.network.id } })
            }
        },
        hideDialog () {
            this.networkDialog = false
            this.submitted = true
        },
        goToNetwork (selectedRows) {
            if (!this.selectionToggle) {
                console.log(selectedRows[0])
                this.setNetwork({ ...selectedRows[0] })
                // this.$toast.add({ severity: 'info', summary: 'Network Selected', detail: 'Name: ' + event.name, life: 3000 })
                this.$router.push({ name: 'networkdetails', params: { id: this.network.id } })
            } else {
                this.selectedNetworks = selectedRows
            }
        }
    }
}
       //  editNetwork (network) {
      //    this.network = { ...network }
      //    this.networkDialog = true
      //  },
      //  confirmDeleteNetwork (network) {
      //    this.network = network
      //    this.deleteNetworkDialog = true
      //  },

      //  async removeNetwork (network) {
      //    this.deleteNetworkDialog = false
      //    this.deleteNetwork({ id: network.id })
      //    // this.network = {}
      //    this.$toast.add({ severity: 'success', summary: 'Succesful', detail: 'Network Deleted', life: 3000 })
      //  },

            //  deleteNetwork () {
      //    this.deleteNetworkDialog = true
      //    this.$store.state.networks = this.$store.state.networks.filter(val => val.id !== this.network.id)
      //    this.network = {}
      //    this.$toast.add({ severity: 'success', summary: 'Succesful', detail: 'Network Deleted', life: 3000 })
      //  },

          //  if (this.network.id) {
          //    this.$store.state.networks[this.findIndexById(this.network.id)] = this.network
          //    this.$toast.add({ severity: 'success', summary: 'Succesful', detail: 'Network updated', life: 3000 })
          //  } else {

      //  findIndexById (id) {
      //      let index = -1
      //      for (let i = 0; i < this.$store.state.networks.length; i++) {
      //          if (this.$store.state.networks[i].id === id) {
      //            index = i
      //              break
      //          }
      //      }
        //    return index
        //  },
 </script>
