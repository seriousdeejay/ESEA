<template>
    <div class="p-d-flex p-grid p-jc-center p-m-0">
        <div class="p-col-12 p-p-3" style="background-color: #dcedc8;">
            <h1>{{survey.name}}</h1>
            <h3>{{survey.description}}</h3>
        </div>

        <div class="p-grid p-col-6 p-p-3">
            <div v-for="topic in survey.topics" :key="topic.id" class="p-grid p-col-12 p-m-3" style="background-color: lightgrey; border-radius: 10px;">
                <div class="p-col-12 p-text-left"><h3>Topic: '{{topic.name}}</h3></div>
                <survey-question
                v-for="question in topic.questions"
                :key="question.id"
                :question="question"
                :answer="answers[question.id]"
                />

                <div v-for="subtopic in topic.sub_topics" :key="subtopic.id" class="p-m-3" style="background-color: white; border-radius: 10px;">
                    <div class="p-col-12 p-text-left"><h3>Topic: '{{subtopic.name}}</h3></div>
                     <survey-question
                    v-for="question in subtopic.questions"
                    :key="question.id"
                    :question="question"
                    :answer="answers[question.id]"
                />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import SurveyQuestion from '../components/survey/SurveyQuestion'
export default {
    components: {
        SurveyQuestion
    },
    data () {
        return {
            topicNumber: 0
        }
    },
    computed: {
        ...mapState('method', ['method']),
        ...mapState('survey', ['survey']),
        ...mapState('surveyResponse', ['surveyResponses', 'surveyResponse']),
        // ...mapState('surveyResponseCalculation', ['surveyResponseCalculations']),
        answers () {
            const answers = {}
            if (this.surveyResponse && this.surveyResponse.question_responses) {
                this.surveyResponse.question_responses.forEach((answer) => {
                    answers[answer.direct_indicator_id] = answer.value
                })
            }
            return answers
        }
        // calculations() {
		// 	const calculations = {};
		// 	if (this.surveyResponseCalculations.length) {
		// 		this.surveyResponseCalculations.forEach((calculation) => {
		// 			calculations[calculation.topic] = !calculations[calculation.topic]
		// 				? [calculation] : [...calculations[calculation.topic], calculation];
		// 		});
		// 	}
		// 	return calculations;
		// },
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
        ...mapActions('surveyResponse', ['fetchSurveyResponses', 'setSurveyResponse']),
        // ...mapActions('surveyResponseCalculation', ['fetchSurveyResponseCalculations']),
        async initialize () {
            await this.fetchSurvey({ mId: this.method.id, id: this.survey.id })
            this.setSurveyResponse(this.surveyResponse[0])
            // await this.fetchSurveyResponseCalculations({ mId: this.method.id, sId: this.survey.id, id: this.surveyResponse.id })
        }
    }
}
</script>
