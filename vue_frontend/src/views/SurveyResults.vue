<template>
    <div class="p-d-flex p-grid p-jc-center p-m-0">
        <div class="p-col-12 p-p-3" style="background-color: #dcedc8;">
            <h1>{{survey.name}}</h1>
            <h3>{{survey.description}}</h3>
            <p>Respondents: {{ surveyResult.respondents }} of {{ surveyResult.all_respondents }} </p>
        </div>
    </div>
    {{surveyResult}}
</template>

<script>
import { mapState, mapActions } from 'vuex'
// import SurveyQuestionResults from '../components/survey/SurveyQuestionResults'
export default {
    components: {
        // SurveyQuestionResults
    },
    data () {
        return {
            topicNumber: 0
        }
    },
    computed: {
        ...mapState('organisation', ['organisation']),
        ...mapState('survey', ['survey']),
        ...mapState('surveyResults', ['surveyResult']),
        answers () {
            return this.surveyResult.question_responses || {}
        },
		calculations () {
			const calculations = {}
			if (this.surveyResult?.calculations.length) {
				this.surveyResult.calculations.forEach((calculation) => {
					calculations[calculation.topic] = !calculations[calculation.topic]
						? [calculation] : [...calculations[calculation.topic], calculation]
				})
			}
            return calculations
        },
        methodId () {
            return parseInt(this.$route.params.id, 10)
        }
    },
    beforeRouteUpdate (to, from, next) {
        this.initialize()
        next()
    },
    created () {
        this.initialize()
    },
    methods: {
        ...mapActions('survey', ['fetchSurvey']),
        ...mapActions('surveyResults', ['fetchSurveyResults']),
        async initialize () {
            const surveyId = parseInt(this.$route.params.surveyId, 10)
            await this.fetchSurvey({ mId: this.methodId, id: surveyId })
            if (this.survey.method !== this.methodId) {
                this.$router.push({ name: 'methods' })
            }
            this.fetchSurveyResults({ mId: this.methodId, sId: surveyId })
        }
    }
}
</script>
