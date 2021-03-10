<template>
    <Toolbar>
        <template #left>
            <ToggleButton v-model="selectionToggle" onLabel="Selecting: Enabled" offLabel="Selecting: Disabled" onIcon="pi pi-check" offIcon="pi pi-times" class="p-mr-2" />
            <Button v-if="createButton && createButton2" label="Create Method" icon="pi pi-plus" class="p-button-success p-mr-2" @click="(importDialog = true)" />
            <Button v-if="addButton && addButton2" :label="addToggle? 'show network methods' : 'add Methods'" class="p-button-success p-mr-2" @click="addToggle? initialize() : addableMethods()" />
            <Button v-if="addToggle" :label="'Add methods'" icon="" class="p-button-primary p-mr-2" @click="selectedRows.length ? addMethods() : ''" :disabled="!selectedRows.length" />
            <Button v-if="removeButton && removeButton2" :label="'Remove Methods'" icon="pi pi-trash" class="p-button-danger" @click="selectionToggle? removeMethods(): RemovableMethods()" :disabled="(!selectionToggle || !selectedRows.length)" />
        </template>

        <template #right>
            <span class="p-input-icon-left">
                <i class="pi pi-search" />
                <InputText v-model="filters['global']" placeholder="Search..." />
            </span>
        </template>
    </Toolbar>

    <DataTable ref="dt" :value="methods" v-model:selection="selectedRows" :selectionMode="selectionToggle? 'multiple' : 'single'" dataKey="id" :metaKeySelection="false" @row-select="goToSelectedMethods"
        :paginator="true" :rows="10" :filters="filters" paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
        :rowsPerPageOptions="[5,10,25]" currentPageReportTemplate="Showing {first} to {last} of {totalRecords} products" class="p-datatable-striped">

        <Column v-for="col of columns" :field="col.field" :header="col.header" :key="col.field" />
    </DataTable>
    <h5 v-if="selectionToggle" class="p-p-3 p-m-3 p-shadow-5">Select the methods you want to add/remove!</h5>

    <Dialog v-model:visible="importDialog" :style="{width: '450px'}" header="Import your Method" :modal="true" class="p-fluid">
        <FileUpload name="myfile" url="http://localhost:8000/import-yaml/" @upload="onUpload" :multiple="true" accept="" :maxFileSize="1000000">
            <template #empty>
                <p>Drag and drop YAML files to here to upload.</p>
            </template>
        </FileUpload>
        <template #footer>
            <Button label="Remove window" icon="pi pi-times" class="p-button-text" @click="importDialog = false"/>
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
                    { field: 'name', header: 'Name' },
                    { field: 'description', header: 'Description' }
                ]
            }
        },
        createButton: {
            type: Boolean,
            default: false
        },
        addButton: {
            type: Boolean,
            default: false
        },
        removeButton: {
            type: Boolean,
            default: false
        }
    },
    data () {
        return {
            importDialog: false,
            selectionToggle: false,
            addToggle: false,
            createButton2: true,
            addButton2: true,
            removeButton2: true,
            selectedRows: [],
            filters: {}
        }
    },

    computed: {
        ...mapState('method', ['methods', 'method']),
        ...mapState('network', ['network'])
    },
    watch: {
        selectedRows: function (val) {
        if (val) {
        console.log(this.selectedRows)
        }
        }
    },
    created () {
        this.initialize()
    },
    methods: {
        ...mapActions('method', ['fetchMethods', 'setMethod']),
        ...mapActions('network', ['patchNetwork']),
        async initialize () {
            await this.fetchMethods({ query: `?network=${this.network?.id || 0}` })
            this.addToggle = false
            this.createButton2 = true
            this.addButton2 = true
            this.removeButton2 = true
        },
        createMethod (event) {
            console.log('create method')
        },
        addableMethods () {
            console.log('check')
            this.fetchMethods({ query: `?excludenetwork=${this.network?.id || 0}` })
            this.selectionToggle = true
            this.addToggle = true
            this.createButton2 = false
            this.removeButton2 = false
        },
        async addMethods () {
            console.log(this.selectedRows)
            await this.patchNetwork({ data: this.selectedRows })
            this.initialize()
        },
        RemovableMethods () {
            this.selectionToggle = true
            this.createButton2 = false
            this.addButton2 = false
        },
        async removeMethods () {
            console.log(this.selectedRows)
            await this.patchNetwork({ data: this.selectedRows })
            this.initialize()
        },
        onUpload () {
            this.initialize()
            this.importDialog = false
        },
        goToSelectedMethods (event) {
            if (!this.selectionToggle) {
                this.setMethod({ ...event.data })
                this.$router.push({ name: 'methoddetails', params: { id: this.method.id } })
            }
       }
    }
}
</script>

        // selectionToggle: {
        //     type: Boolean,
        //     default: true
        // }

    // },
        // onRowSelect (event) {
        //     this.$emit('item-redirect', this.selectedRows)
        // },
