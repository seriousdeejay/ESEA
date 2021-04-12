<template>
    <Toolbar>
        <template #left>
            <Button label="Create Method" icon="pi pi-plus" class="p-button-success p-mr-2" @click="importDialog = true" />
            <div v-if="networkMethods">
                <div v-if="!addingProcess">
                        <ToggleButton v-if="selectionEnabled" v-model="selectionToggle" onLabel="Selecting: Enabled" offLabel="Selecting: Disabled" onIcon="pi pi-check" offIcon="pi pi-times" class="p-mr-2" />
                        <Button label="Add Methods" icon="pi pi-plus" class="p-button-success p-mr-2" @click="addableMethods()" />
                        <Button label="Remove Methods" icon="pi pi-trash" class="p-button-danger" @click="confirmationDialog = true" :disabled="!selectedRows.length" />
                </div>
                <div v-else>
                    <Button label="Show network methods" class="p-button-success p-mr-2" @click="initialize()" />
                    <Button label="Add selected Methods" class="p-button-primary p-mr-2" @click="confirmationDialog = true" :disabled="!selectedRows.length" />
                </div>
            </div>
        </template>

        <template #right>
            <span class="p-input-icon-left">
                <i class="pi pi-search" />
                <InputText v-model="filters['global']" placeholder="Search..." />
            </span>
        </template>
    </Toolbar>
    <div v-if="methods.length">
        <DataTable ref="dt" :value="methods" v-model:selection="selectedRows" :selectionMode="selectionToggle? 'multiple' : 'single'" dataKey="id" :metaKeySelection="false" @row-select="goToSelectedMethods"
            :paginator="true" :rows="10" :filters="filters" paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
            :rowsPerPageOptions="[5,10,25]" currentPageReportTemplate="Showing {first} to {last} of {totalRecords} products" class="p-datatable-striped">

            <Column v-for="col of columns" :field="col.field" :header="col.header" :key="col.field" />
        </DataTable>
    </div>
    <div v-else class="p-p-3 p-text-bold"> {{addingProcess? 'There are no methods to add, create one first!' : 'This network has no methods, add one!'}}</div>

    <Dialog v-model:visible="confirmationDialog" :style="{width: '450px'}" header="Confirm" :modal="true">
      <div class="confirmation-content">
          <i class="pi pi-exclamation-triangle p-mr-3" style="font-size: 2rem" />
            <span v-if="networkMethods">Are you sure you want to <b>{{addingProcess? 'add' : 'remove'}}</b> the following methods?</span>
            <span v-else>Are you sure you want to <b>delete</b> the following methods?</span>
            <br>
            <div class="p-shadow-2 p-m-3 p-p-3">
            <div v-for="item in selectedRows" :key=item.name>{{item.name}}</div>
            </div>
      </div>
      <template #footer>
        <Button label="No" icon="pi pi-times" class="p-button-text" @click="(confirmationDialog = false) && (selectedRows = [])"/>
        <Button v-if="networkMethods" label="Yes" icon="pi pi-check" class="p-button-text" @click="addingProcess? addMethods() : removeMethods()" />
        <Button v-else label="Yes" icon="pi pi-check" class="p-button-text" @click="deleteMethods()" />
      </template>
    </Dialog>

    <Dialog v-model:visible="importDialog" :style="{width: '450px'}" header="Import your Method" :modal="true" class="p-fluid">
        <FileUpload name="myfile" :customUpload="true" @uploader="onUpload" :fileLimit="1" accept=".yaml" :maxFileSize="1000000">
            <template #empty>
                <p>Drag and drop your YAML file here to upload.</p>
            </template>
        </FileUpload>
        <template #footer>
            <Button label="Remove window" icon="pi pi-times" class="p-button-text" @click="importDialog = false"/>
        </template>
    </Dialog>
</template>

<script>
import { AxiosInstance } from '../plugins/axios'
import { mapActions, mapState } from 'vuex'

export default {
    props: {
        columns: {
            type: Array,
            default: function () {
                return [
                    { field: 'name', header: 'Name' },
                    { field: 'description', header: 'Description' },
                    { field: '', header: '' }
                ]
            }
        },
        networkMethods: {
            type: Boolean,
            default: false
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
            confirmationDialog: false,
            importDialog: false
        }
    },
    computed: {
        ...mapState('method', ['methods', 'method']),
        ...mapState('network', ['network'])
    },
    created () {
        this.initialize()
    },
    methods: {
        ...mapActions('method', ['fetchMethods', 'setMethod', 'uploadMethod']),
        ...mapActions('network', ['patchNetwork']),
        async initialize () {
            if (this.networkMethods) {
                console.log('eee')
                this.fetchMethods({ query: `?network=${this.network?.id || 0}` })
            } else {
                this.fetchMethods({})
            }
            this.selectedRows = []
            this.confirmationDialog = false
            this.addingProcess = false
        },
        createMethod (event) {
            console.log('create method')
        },
        addableMethods () {
            this.fetchMethods({ query: `?excludenetwork=${this.network?.id || 0}` })
            this.addingProcess = true
            this.selectionToggle = true
        },
        async addMethods () {
            await this.patchNetwork(this.selectedRows)
            this.initialize()
        },

        async removeMethods () {
            await this.patchNetwork(this.selectedRows)
            this.selectedRows.forEach((method, i) => {
                this.$toast.add({ severity: 'success', summary: 'The following method was removed', detail: `${method.name}`, life: 3000 })
            })
            this.initialize()
        },
        async deleteMethods () {
            await this.selectedRows.forEach((method, i) => {
                this.deleteOrganisation({ id: method?.id || 0 })
                this.$toast.add({ severity: 'success', summary: 'The following method was deleted', detail: `${method.name}`, life: 3000 })
            })
        },
        async onUpload (event) {
            // for (const file of event.files) {
            //     console.log(file)
            // }
            var formData = new FormData()
            formData.append('file', event.files[0])
            return new Promise((resolve, reject) => {
            AxiosInstance.post('/import-yaml/', formData)
            .then(response => {
                this.importDialog = false
                this.$toast.add({ severity: 'success', summary: 'Method created', detail: 'New method', life: 3000 })
                this.initialize()
            resolve()
            })
            .catch(err => { reject(err) })
            })
        },
        goToSelectedMethods (event) {
            this.$toast.add({ severity: 'info', summary: 'Method Selected', detail: `${event.data.name}`, life: 3000 })
            if (!this.selectionToggle) {
                this.setMethod({ ...event.data })
                this.$router.push({ name: 'methoddetails', params: { id: event.data.id } })
                this.$router.push({ name: 'networkmethod', params: { NetworkId: this.network.id, MethodId: this.method.id } })
            }
       }
    }
}
</script>
