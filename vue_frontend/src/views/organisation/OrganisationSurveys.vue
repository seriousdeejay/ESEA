<template>
    <div v-if="surveys">
                <DataTable ref="dt" :value="surveys" v-model:selection="selectedRows" :selectionMode="selectionToggle? 'multiple' : 'single'" dataKey="id" :metaKeySelection="false" @row-select="onRowSelect"
        :paginator="true" :rows="10" :filters="filters" paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
        :rowsPerPageOptions="[5,10,25]" currentPageReportTemplate="Showing {first} to {last} of {totalRecords} products" class="p-datatable-striped">

            <!-- <h1>{{tableName}}</h1> -->
            <Column v-for="col of columns" :field="col.field" :header="col.header" :key="col.field"></Column>
        </DataTable>
    </div>
    <div v-else class="p-text-italic">
        Your organisation has no surveys to display.<br> Join a network to get available surveys!
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
    components: {
    },
    data () {
        return {
            columns: [
                { field: 'name', header: 'Name' },
                { field: 'description', header: 'Description' },
                { field: 'questions.length', header: 'Questions' },
                { field: 'method', header: 'Method' },
                { field: 'stakeholder', header: 'Stakeholder group' }
            ]
        }
    },
    computed: {
        ...mapState('survey', ['surveys']),
        ...mapState('method', ['methods'])
    },
    created () {
        this.initialize()
    },
    methods: {
        ...mapActions('survey', ['fetchSurveys']),
        ...mapActions('method', ['fetchMethods']),
        async initialize () {
            await this.fetchMethods({})
            for (const method of this.methods) {
                await this.fetchSurveys({ mId: method.id, query: `?organisation=${this.$route.params.OrganisationId}` })
            }
        }
    }
}
</script>
