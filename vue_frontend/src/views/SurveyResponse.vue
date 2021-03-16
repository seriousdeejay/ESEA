<template>
<div class="p-d-flex p-grid p-jc-center p-m-0">
    <div class="p-col-12 p-p-3" style="background-color: #dcedc8;">
        <h1>{{survey.name}}</h1>
        <h3>{{survey.description}}</h3>
        {{surveyResponse}}
    </div>
    <div class="p-grid p-col-6 p-p-3" style="background-color: white; border-radius: 10px;">
        <div class="p-col-6 p-text-left">Topic {{ topicNumber + 1}} of {{totalTopics}}</div>
        <div class="p-col-6 p-text-right"><ProgressBar :value="progressBarValue">{{progressBarValue}}% completed</ProgressBar></div>
        <div class="p-col-12 p-text-left"><h3>Topic: '{{currentTopic.name}}'</h3></div>
        <survey-question class="p-col-12"
        v-for="question in currentTopic.questions"
        :key="question.id"
        :question="question"
        :answer="answers[question.id]"
        @input="updateAnswer(question.id, $event)"
        />

    <div class="p-col-6 p-text-left">
        <Button label="Previous Topic" class="p-button-raised p-button-sm" :disabled="topicNumber === 0" @click="previousTopic"/>
    </div>
    <div class="p-col-6 p-text-right">
        <Button v-if="topicNumber + 1 < totalTopics" label="Next Topic" class="p-button-raised p-button-sm" @click="nextTopic" />
        <Button v-else label="Finish Survey" class="p-button-success p-button-raised p-button-sm" @click="finishSurvey" />
    </div>
    </div>
</div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import SurveyQuestion from '../components/survey/SurveyQuestion'
import ProgressBar from 'primevue/progressbar'

export default {
    components: {
        SurveyQuestion,
        ProgressBar
    },
    data () {
        return {
        topicNumber: 0,
        progressBarValue: 0,
        radiovalue: null
        }
    },
    computed: {
        ...mapState('method', ['method']),
        ...mapState('survey', ['survey']),
        ...mapState('surveyResponse', ['surveyResponses', 'surveyResponse']),
        currentTopic () {
            return this.survey?.topics[0].sub_topics[this.topicNumber]
        },
        totalTopics () {
            let totalTopics = 0
            for (const topic in this.survey?.topics) {
                totalTopics = totalTopics + this.survey?.topics[topic].sub_topics.length
            }
            return totalTopics
        },
        answers () {
            const answers = {}
            if (this.surveyResponse?.id !== this.survey.id && this.surveyResponse.question_responses) {
                this.surveyResponse.question_responses.forEach((answer) => {
                    answers[answer.direct_indicator_id] = answer.value
                })
            }
            return answers
        }
    },
    created () {
        this.initialize()
    },
    methods: {
        ...mapActions('survey', ['fetchSurvey']),
        ...mapActions('surveyResponse', ['fetchSurveyResponses', 'setSurveyResponse', 'updateSurveyResponse', 'createSurveyResponse']),
        async initialize () {
            await this.fetchSurvey({ mId: this.method.id, id: this.survey.id })
            await this.fetchSurveyResponses({ mId: this.method.id, sId: this.survey.id })
            if (this.surveyResponses.length) {
				this.setSurveyResponse(this.surveyResponses[1])
				return
            }
            this.createSurveyResponse({ mId: this.method.id, sId: this.survey.id })
        },
        progress (pageturn) {
            var interval = 100 / this.totalTopics
            if (pageturn === 'back') {
                this.progressBarValue -= interval
            }
            if (pageturn === 'next') {
                this.progressBarValue += interval
            }
        },
        previousTopic () {
            if (this.topicNumber > 0) {
                this.topicNumber -= 1
                this.progress('back')
            }
        },
        nextTopic () {
            if (this.topicNumber + 1 < this.totalTopics) {
                this.topicNumber += 1
                this.progress('next')
            }
        },
        finishSurvey () {
            console.log(this.surveyResponse)
            this.updateSurveyResponse({ mId: this.method.id, sId: this.survey.id, surveyResponse: { ...this.surveyResponse } })
            this.$router.push({ name: 'method-survey-result', params: { OrganisationId: this.$route.params.OrganisationId, id: this.method.id, surveyId: this.survey.id } })
        },
        updateAnswer (id, answer) {
            this.updateSurveyResponse({
                mId: this.method.id,
                sId: this.survey.id,
                surveyResponse: {
                    ...this.surveyResponse,
                    question_responses: [
                        ...this.surveyResponse.question_responses,
                        { direct_indicator_id: id, value: answer }
                    ]
                }
            })
        }
    }
}
</script>
