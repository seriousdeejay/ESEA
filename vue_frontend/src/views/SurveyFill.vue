<template>
    <div v-if="!surveyResponse.finished" class="p-d-flex p-grid p-jc-center p-m-0">
        <div class="p-col-12 p-p-3" style="background-color: #dcedc8;">
            <h1>{{survey.name}}</h1>
            <h3>{{survey.description}}</h3>
            {{survey}}
            <p><span class="p-text-bold">Respondent:</span> {{surveyResponse.respondent}} <br> <span class="p-text-bold">Organisation:</span>{{surveyResponse.organisation}} </p>
        </div>
        <div class="p-grid p-col-6 p-p-3" style="background-color: white; border-radius: 10px;">
            <div class="p-col-6 p-text-left">Topic {{ topicNumber + 1}} of {{totalTopics}}</div>
            <div class="p-col-6 p-text-right"><ProgressBar :value="progress">{{progress}}% completed</ProgressBar></div>
            <div class="p-col-12 p-text-left"><h3>Topic: '{{currentTopic.name}}'</h3></div>
            <survey-question class="p-col-12"
            v-for="question in currentTopic.questions"
            :key="question.id"
            :question="question"
            :answer="answers[question.id]"
            :checkanswerrequired="question.isMandatory"
            @input="updateAnswer(question.id, $event)"
            />
        <div class="p-col-6 p-text-left">
            <Button label="Previous Topic" class="p-button-raised p-button-sm" :disabled="topicNumber === 0" @click="previousTopic"/>
        </div>
        <div class="p-col-3 p-text-right">
            <Button label="Save for Now" class="p-button-primary p-button-raised p-button-sm" @click="saveSurvey" />
        </div>
        <div class="p-col-3 p-text-right">
            <Button v-if="topicNumber + 1 < totalTopics" label="Next Topic" class="p-button-raised p-button-sm" style="width: 100%" @click="nextTopic" />
            <Button v-else label="Finish Survey" class="p-col p-button-success p-button-raised p-button-sm" style="width: 100%" @click="finishSurvey" />
        </div>
        </div>
    </div>

    <Dialog v-model:visible="missedQuestionsDialog" :style="{width: '450px'}" header="Missing Answers" :modal="true">
        <i class="pi pi-star p-mr-3" style="font-size: 1.5rem" />
        <span class="p-text-left">You need to fill in the following answers to be able to send your survey response:</span>
        <div class="p-grid p-m-2">
            <div v-for="question, i in missedQuestions" :key="question" class="p-col-3">
                <Button :label="`${i+1}`" @click="goToQuestion(question)"> </Button>
            </div>
        </div>
        <template #footer>
            <Button label="Ok" class="p-button-text" @click="missedQuestionsDialog = false"/>
        </template>
    </Dialog>
</template>
<script>
import { mapActions, mapState } from 'vuex'
import SurveyQuestion from '../components/survey/SurveyQuestion'
import ProgressBar from 'primevue/progressbar'

// import axios from 'axios'
// import { AxiosInstance } from '../plugins/axios'
export default {
    components: {
        SurveyQuestion,
        ProgressBar
    },
    data () {
        return {
            topicNumber: 0,
            progressBarValue: 0,
            // currentanswer: null,
            checkAnswerRequired: false,
            missedQuestions: [],
            missedQuestionsDialog: false
        }
    },
    computed: {
        ...mapState('survey', ['survey']),
        ...mapState('surveyResponse', ['surveyResponse', 'surveyResponses']),
        ...mapState('eseaAccount', ['eseaAccount']),
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
                    answers[answer.direct_indicator_id] = [answer.values, answer.value]
                })
            }
            console.log(answers)
            return answers
        },
        progress () {
            var progress
            progress = (this.topicNumber / this.totalTopics) * 100
            return progress
        }

    },
    created () {
        this.initialize()
    },
    methods: {
        ...mapActions('survey', ['fetchSurvey']),
        ...mapActions('surveyResponse', ['fetchSurveyResponse', 'setSurveyResponse', 'updateSurveyResponse', 'createSurveyResponse', 'setSurveyResponse']),
        async initialize () {
    //   axios.get('http://127.0.0.1:8000/methods/27/surveys/13/organisations/1/responses/')
    //   .then(response => (console.log(response)))
    //    AxiosInstance.get('/methods/27/surveys/13/organisations/1/responses/GhjrpoLc/', {}).then(response => (console.log(response)))
            await this.setSurveyResponse({})
            await this.fetchSurveyResponse({ nId: 0, cId: 0, eaId: this.eseaAccount.id || 0, id: this.$route.params.uniquetoken }) // this.$route.params.uniquetoken
            await this.fetchSurvey({ mId: this.surveyResponse.method, id: this.surveyResponse.survey })
            if (this.surveyResponse.finished) {
                this.$router.push({ name: 'survey-thank-you' })
            }
        },
        previousTopic () {
            if (this.topicNumber > 0) {
                this.topicNumber -= 1
            }
        },
        nextTopic () {
            if (this.topicNumber + 1 < this.totalTopics) {
                this.topicNumber += 1
            }
        },
        goToQuestion (question) {
            this.topicNumber = 0
            for (var subtopic of this.survey.topics[0].sub_topics) {
                if (subtopic.questions[0].id === question) {
                    break
                }
                this.topicNumber = this.topicNumber + 1
            }
            this.missedQuestionsDialog = false
        },
        saveSurvey () {
            // TODO // popup Dialog: Survey is automatically saved.
        },
        finishSurvey () {
            const mandatorydict = {}
            this.missedQuestions = []
            this.survey.topics[0].sub_topics.forEach(SubTopic => { mandatorydict[SubTopic.questions[0].id] = SubTopic.questions[0].isMandatory })
            this.surveyResponse.question_responses.forEach(response => { if (mandatorydict[response.direct_indicator_id]) { if (!response.values.length && !response.value) { this.missedQuestions.push(response.direct_indicator_id) } } })

            if (!this.missedQuestions.length) {
            this.surveyResponse.finished = true
            console.log('kkk', this.surveyResponse)
            this.updateSurveyResponse({ nId: 1, cId: 1, eaId: 1, surveyResponse: { ...this.surveyResponse } })
            console.log(this.surveyResponse.finished)
            this.$router.push({ name: 'survey-thank-you' })
            } else {
                this.missedQuestionsDialog = true
                // TODO // popup Dialog: You forgot to fill in the following required questions
            }
        },
        async updateAnswer (id, answer) {
            // this.currentanswer = answer
            console.log('rrrrrrrrrr', answer)
            if ((this.$route.params.uniquetoken !== this.surveyResponse.token) && (this.$route.params.uniquetoken !== 'accountant')) {
                console.log('Not possible')
                return
            }
            console.log('sss', this.surveyResponse)
            this.surveyResponse.question_responses.forEach(response => { if (response.direct_indicator_id === id) { if (answer.answer[0] != null) { if (answer.answertype === ('RADIO' || 'CHECKBOX')) { response.values = answer.answer } else { response.value = answer.answer[0] } } } })
            await this.updateSurveyResponse({
                nId: 1,
                cId: 1,
                eaId: 1,
                surveyResponse: {
                    ...this.surveyResponse
                }
            })
            console.log('lll', this.surveyResponse)
        }
    }
}
</script>
