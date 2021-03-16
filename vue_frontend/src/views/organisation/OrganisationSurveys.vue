<template>
    <div v-if="surveys.length">
                <DataTable ref="dt" :value="surveys" v-model:selection="selectedRows" :selectionMode="selectionToggle? 'multiple' : 'single'" dataKey="id" :metaKeySelection="false" @row-select="goToSurvey"
        :paginator="true" :rows="10" :filters="filters" paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
        :rowsPerPageOptions="[5,10,25]" currentPageReportTemplate="Showing {first} to {last} of {totalRecords} products" class="p-datatable-striped">

            <!-- <h1>{{tableName}}</h1> -->
            <!-- <Column v-for="col of columns" :field="col.field" :header="col.header" :key="col.field"></Column> -->
            <Column field="name" header="Name"></Column>
            <Column field="description" header="Description"></Column>
            <Column field="questions.length" header="Questions"></Column>
            <Column field="method" header="Method"></Column>
            <Column field="stakeholders" header="Stakeholder group"></Column>
            <Column header="Results">
                <template #body="slotProps">
                    <Button type="button" label="Results" class="p-button-raised p-button secondary" @click="goToSurveyResult(slotProps.data)" :disabled="existingsurveyresult"/>
                </template>
            </Column>
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
                { field: 'stakeholders', header: 'Stakeholder group' }
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
        ...mapActions('survey', ['fetchSurveys', 'setSurvey']),
        ...mapActions('method', ['fetchMethods']),
        ...mapActions('surveyResponse', ['fetchSurveyResponses']),
        async initialize () {
            await this.fetchMethods({})
            for (const method of this.methods) {
                await this.fetchSurveys({ mId: method.id, query: `?organisation=${this.$route.params.OrganisationId}` })
            }
        },
        async goToSurvey (survey) {
            console.log(survey.data)
            console.log(survey.data.id)
            console.log(survey.data.method.id)
            // this.$router.push({ name: 'method-survey-result', params: { id: this.method.id, surveyId: survey.id } })
            await this.setSurvey(survey.data)
            this.$router.push({ name: 'survey-fill', params: { id: 27, surveyId: survey.data.id } })
        },
        async goToSurveyResult (row) {
            await this.fetchSurveyResponses({ mId: 27, sId: row.id })
            this.$router.push({ name: 'method-survey-result', params: { OrganisationId: this.$route.params.OrganisationId, id: 27, surveyId: row.id } })
        }
    }
}
</script>
