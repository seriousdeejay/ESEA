<template>
    <DataTable :value="surveys" :filters="filters2">
        <template #header>
            <div class="p-d-flex p-jc-between p-ai-center">
                <h3 class="p-m-0">Surveys</h3>
                <span class="p-input-icon-left"> <i class="pi pi-search" />
                    <InputText v-model="filters2['global']" placeholder="Keyword Search" />
                </span>
            </div>
    </template>
         <Column v-for="col of columns" :field="col.field" :header="col.header" :key="col.field" />
    </DataTable>
    <Divider class="p-my-5" />
    <DataTable :value="surveyResponses" :filters="filters" selectionMode="single" @row-select="goToSurveyResponse" >
        <div class="p-d-flex p-jc-between p-ai-center">
            <h3 class="p-m-0">Survey Responses</h3>
            <span class="p-input-icon-left"> <i class="pi pi-search" />
                <InputText v-model="filters['global']" placeholder="Keyword Search" />
            </span>
        </div>
        <Column v-for="col of responsecolumns" :field="col.field" :header="col.header" :key="col.field" />
    </DataTable>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
    components: {
    },
    data () {
        return {
            filters: {},
            filters2: {},
            // filters: {
            //     surveys: { value: null },
            //     surveyresponses: { value: null }
            // },
            columns: [
                { field: 'name', header: 'Name' },
                { field: 'description', header: 'Description' },
                { field: 'questions.length', header: 'Questions' },
                { field: 'method.name', header: 'Method' },
                { field: 'stakeholders', header: 'Stakeholder group' }
            ],
            responsecolumns: [
                { field: 'survey', header: 'Survey' },
                { field: 'user_organisation.user', header: 'Participant' },
                { field: 'user_organisation.organisation', header: 'Organisation' },
                { field: 'user_organisation.stakeholdergroups', header: 'Stakeholder Groups' }
            ]
        }
    },
    computed: {
        ...mapState('method', ['method']),
        ...mapState('survey', ['surveys']),
        ...mapState('surveyResponse', ['surveyResponses'])
    },
    created () {
        this.initialize()
    },
    methods: {
        ...mapActions('survey', ['fetchSurveys']),
        ...mapActions('surveyResponse', ['fetchSurveyResponses', 'setSurveyResponse']),
        async initialize () {
            this.fetchSurveys({ mId: this.method?.id || 0 })
            this.fetchSurveyResponses({ mId: this.method?.id, sId: 0 })
        },
        async goToSurveyResponse (event) {
            console.log(event.data)
            await this.setSurveyResponse({ ...event.data })
            this.$router.push({ name: 'method-survey-result', params: { OrganisationId: 'Needs some value', id: this.method.id, surveyId: event.data.id } })
        }
    }
}
</script>
