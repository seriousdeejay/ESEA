<template>
<div class="p-d-flex p-grid p-jc-center p-m-0">
    <div class="p-col-12 p-p-3" style="background-color: #dcedc8;">
        <h1>{{survey.name}}</h1>
        <h3>{{survey.description}}</h3>
    </div>
    <div class="p-grid p-col-6 p-p-3" style="background-color: white; border-radius: 10px;">
        <div class="p-col-6 p-text-left">Topic {{ topicNumber + 1}} of {{totalTopics}}</div>
        <div class="p-col-6 p-text-right">Progress bar here</div>
        <div class="p-col-12 p-text-left"><h3>Topic: '{{currentTopic.name}}'</h3></div>
        <survey-question
        v-for="question in currentTopic.questions"
        :key="question.id"
        :question="question"
        :answer="answers[question.id]"
        @input="updateAnswer(question.id, $event)"
        />
            <!-- <div v-for="question in currentTopic.questions" :key="question.id">
                <div class="p-text-left">{{question.name}}</div>
                <div v-for="option in question.options" :key="option.id" class="p-field-radiobutton">
                <RadioButton :id="option.id" name="option" :value="option.text" v-model="radiovalue" />
                <label :for="option.id">{{option.text}}</label>
                </div>
                {{radiovalue}}
                <div v-for="option in question.options" :key="option.id">
                                <div class="p-shadow-2 p-p-3 p-my-2">{{option.text}}</div>
                            </div>
                <br>
                <br>
                <div v-if="question.description" class="p-text-justify p-p-2" style="background-color: #FAFAFA;">
                    {{question.description}}</div>
            </div> -->
        <!-- <div class="p-col-12" v-for="subtopic in survey.topics[0].sub_topics" :key="subtopic.id">
            {{subtopic.name}}

            <div v-for="question in subtopic.questions" :key="question.id">
            </div>
        <br>
        </div> -->
        <div class="p-col-6 p-text-left">
            <Button label="Previous Topic" class="p-button-raised p-button-sm" :disabled="topicNumber === 0" @click="previousTopic"/>
        </div>
        <div class="p-col-6 p-text-right">
            <Button v-if="topicNumber + 1 < totalTopics" label="Next Topic" class="p-button-raised p-button-sm" @click="nextTopic" />
            <Button v-else label="Finish Survey" class="p-button-success p-button-raised p-button-sm" @click="finishSurvey" />
        </div>
    </div>
    <!-- {{survey.topics[0].sub_topics[0].questions[0].name}} -->
    <!-- <div class="p-grid nasted-grid" style="width: 1000px">

        <div class="p-shadow-5">
            <div v-for="topic in survey.sub_topics" :key="topic.id">
                <p>{{topic.name}}</p>
            </div>
        </div>
    </div> -->
</div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import SurveyQuestion from '../components/survey/SurveyQuestion'

export default {
    components: {
        SurveyQuestion
    },
    data () {
        return {
        topicNumber: 0,
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
            var totalTopics = 0
            for (const topic in this.survey?.topics) {
                for (const subtopic in this.survey?.topics[topic].sub_topics) {
                    totalTopics = totalTopics + 1
                    console.log(subtopic)
                    }
                    console.log(this.survey.topics[topic])
            }
            return totalTopics
        },
        answers () {
            const answers = {}
            if (this.surveyResponse?.id !== this.surveyId && this.surveyResponse.question_responses) {
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
        finishSurvey () {
            console.log(this.surveyResponse)
            this.updateSurveyResponse({ mId: this.method.id, sId: this.survey.id, surveyResponse: { ...this.surveyResponse } })
            this.$router.push({ name: 'method-survey-result', params: { id: this.method.id, surveyId: this.survey.id } })
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
