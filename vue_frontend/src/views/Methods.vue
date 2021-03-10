<template>
    <div class="methods">
        <h1>Methods Overview</h1>
        <Toast position="top-right"/>
        <div class="card p-m-5 p-shadow-2">
            <DataTable ref="dt" :value="methods" v-model:selection="selectedMethods" selectionMode="single" dataKey="id" @row-select="goToMethod"
            :paginator="true" :rows="10" :filters="filters" paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
            :rowsPerPageOptions="[5,10,25]" currentPageReportTemplate="Showing {first} to {last} of {totalRecords} products" class="p-datatable-striped">

            <Toolbar>
                <template #left>
                    <Button label="Create Method" icon="pi pi-plus" class="p-button-success p-mr-2" @click="openCreateMethodDialog" />
                    <Button label="Import YAML" icon="pi pi-upload" class="p-button-success" @click="importDialog=true" />
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
              <!--<Column field="organisations.length" header="Organisations" :sortable="true"></Column>
              <Column field="" header="Created by" :sortable="true"></Column> Created_by attribute needs to be added to the Method model -->
            </DataTable>
        </div>
    </div>

    <Dialog v-model:visible="methodDialog" :style="{width: '450px'}" header="Method Details" :modal="true" class="p-fluid">
        <div class="p-field">
            <label for="name">Name</label>
            <InputText id="name" v-model.trim="method.name" required="true" autofocus :class="{'p-invalid': submitted && !method.name}"
            @blur="updateMethodForm({ name: $event.target.value })" />
            <small class="p-error" v-if="submitted && !method.name">Name is required.</small>
        </div>
        <div class="p-field">
            <label for="description">Description</label>
            <Textarea id="description" v-model="method.description" required="true" rows="3" cols="20"
            @blur="updateMethodForm({ description: $event.target.value })" />
        </div>
        <div class="p-field">
            <label for="ispublic">Should this method be public? </label>
            <SelectButton id="ispublic" v-model="method.ispublic" required="true" :options="ispublicbool"
            @blur="updateMethodForm({ ispublic: $event.target.value })" />
        </div>
        <template #footer>
            <Button label="Cancel" icon="pi pi-times" class="p-button-text" @click="hideDialog"/>
            <Button label="Save" icon="pi pi-check" class="p-button-text" @click="saveMethod" :disabled="!method.name" />
        </template>
    </Dialog>

    <Dialog v-model:visible="importDialog" :style="{width: '450px'}" header="Import a Method" :modal="true" class="p-fluid">
        <FileUpload name="myfile" url="http://localhost:8000/import-yaml/" @upload="onUpload" :multiple="true" accept="" :maxFileSize="1000000">
            <template #empty>
                <p>Drag and drop files to here to upload.</p>
            </template>
        </FileUpload>
        <template #footer>
            <Button label="Remove window" icon="pi pi-times" class="p-button-text" @click="importDialog = false"/>
        </template>
    </Dialog>

    <!-- <div>
        <h1>
        to do:
        -List of Methods (just like Method and Organisations)
        </h1>
    </div>
    <div style="margin: 0px 50px">
         <h1>Manage Methods</h1>
        <div class="p-grid">
            <div v-for="organisation in APIData" :key="organisation.id"  class="p-col-4">
                <div v-if="organisation.ispublic">
                <Card style="margin-bottom: 2em" class="p-shadow-5">
                    <template #title>
                        {{ organisation.name }}
                    </template>
                    <template #content>
                        <p> {{ organisation.description }}</p>
                        <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
                    </template>
                    <template #footer>
                        <div class="p-d-flex">
                        <Button icon="pi pi-chevron-down" label="View" />
                        <Button icon="pi pi-pencil" label="Edit" @click="$router.push({name: 'organisationdetails', params: { id: organisation.id }})" class="p-button-secondary" style="margin-left: .5em" />
                         <p class="p-ml-auto">{{ organisation.creator }} 9 min</p>
                        </div>
                    </template>
                </Card>
                </div>
                <div v-else>Private Post</div>
            </div>
        </div>
    </div> -->
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
    // onIdle () {
    //   this.$store.dispatch('userLogout')
    //     .then(() => {
    //       this.$router.push({ name: 'login' })
    //     })
    // },
    data () {
        return {
            filters: {},
            ispublicbool: ['true', 'false'],
            methodDialog: false,
            importDialog: false,
            submitted: false,
            selectedMethods: null
        }
    },
    computed: {
        ...mapState('method', ['methods', 'method'])
    },
    created () {
        this.initialize()
    },
    methods: {
        ...mapActions('method', ['fetchMethods', 'setMethod', 'createMethod', 'updateMethodForm']),
        async initialize () {
            await this.fetchMethods({})
        },
        async openCreateMethodDialog () {
            this.setMethod({})
            this.methodDialog = true
            this.submitted = true
        },
        onUpload () {
            this.initialize()
            this.importDialog = false
        },
        saveMethod () {
            this.submitted = true
            if (this.method.name.trim()) {
                this.createMethod({})
                this.$toast.add({ severity: 'success', summary: 'Succesful', detail: 'Method created', life: 3000 })
            }
            this.methodDialog = true
        },
        goToMethod (event) {
            console.log(this.selectedMethods)
            this.setMethod(this.selectedMethods)
            console.log(this.method)
            this.$router.push({ name: 'methoddetails', params: { id: this.method.id } })
        }
    }
}
</script>
