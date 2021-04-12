<template>
    <div class="p-d-flex p-grid p-jc-center p-m-0">
        <div class="p-col-12 p-p-3" style="background-color: #dcedc8;">
            <h1>{{method.name}}</h1>
            <h3>{{method.description}}</h3>
        </div>
        <div class="p-grid p-col-6 p-p-3" style="min-width: 800px;">
            <SelectButton v-model="amountDisplayButtonValue" :options="amountDisplayButtonOptions" optionLabel="name" class="p-col-12" style="min-width: 500px;" />
            <div v-if="amountDisplayButtonValue.value === 1">
                <div v-for="survey in method.surveys" :key="survey.id" class="p-col-12 p-my-5" style="background-color: #F5F5F5; border-radius: 10px;">
                    <h3>Survey: <span class="p-text-light">{{survey.name}}</span></h3>
                    <div v-for="topic in survey.topics" :key="topic.id" class="p-grid p-col-12 p-p-3" >
                        <div class="p-col-12 p-text-left"><h3>Topic: {{topic.name}}</h3></div>
                        <!-- <survey-question
                        v-for="question in topic.questions"

                        :key="question.id"
                        :question="question"
                        :answer="0"
                        :readonly="true"
                        /> -->

                        <div v-for="subtopic in topic.sub_topics" :key="subtopic.id" class="p-col-12 p-my-3" style="background-color: white; border-radius: 10px;">
                            <h3 class="p-col-12 p-text-left">Topic: <span class="p-text-light">{{subtopic.name}}</span></h3>
                            <div v-for="question in subtopic.questions" :key="question.id" class="p-p-5" style="border: 1px solid lightgrey">
                                <p class="p-text-left"><span v-if="question.isMandatory" style="color: red; font-size: 25px">*</span><span class="p-text-bold">Question:</span> {{question.name}}</p>
                                <Divider />
                                <div v-if="question.answertype === 'SCALE' ||'RADIO'">
                                    <div v-for="(option, index) in question.options" :key="`${index}-option`" class="p-field-radiobutton">
                                        <RadioButton :id="`${index}-option`" name="option" :value="option[optionValueKey]" v-model="lazyValue" :disabled="readonly" required/>
                                        <label :for="`${index}-option`" class="p-text-left">{{option.text}}</label>
                                    </div>
                                </div>
                                <div v-if="question.answertype === 'CHECKBOX'">
                                    <div v-for="(option, index) in question.options" :key="`${index}-option`" class="p-field-checkbox">
                                        <Checkbox :id="`${index}-option`" name="option" :value="option[optionValueKey]" v-model="lazyValue" disabled="true" required/>
                                        <label :for="`${index}-option`" class="p-text-left">{{option.text}}</label>
                                    </div>

                                </div>
                                <div v-if="question.answertype === ('NUMBER' || 'TEXT')">
                                    <InputText type="text" :placeholder="question.answertype.toLowerCase()" disabled class="p-field-checkbox"></InputText>
                                </div>
                                <Divider />
                                <div v-if="question.description">
                                    <p class="p-text-justify p-text-light p-m-0" style="color: lightgrey;"><small>Description:</small><br>
                                    <small><small>{{question.description}}</small></small></p>
                                </div>
                                <div v-else>
                                    <p class="p-text-left p-m-0" style="color: lightgrey;"><small>No Description</small></p>
                                </div>

                                <!-- <div class="p-p-5" style="border-color: #00008B; border: 1px solid lightgrey; border-radius: 5px;">
                    <p class="p-text-left">{{question.name}}</p>
                    <Divider />
                    <div v-if="question.description">
                        <p class="p-text-justify p-text-light p-m-0" style="color: lightgrey;"><small>Description:</small><br>
                        <small><small>{{question.description}}</small></small></p>
                    </div>
                    <div v-else>
                        <p  class="p-text-left p-m-0" style="color: lightgrey;"><small>No Description</small>
                        </p></div>
        </div>
                                {{question.isMandatory}}
                                {{question.name}}
                                {{question.description}}
                                {{question.answertype}}
                                <div v-for="option in question.options" :key="option.id">
                                    {{option.text}}
                                </div> -->
                            </div>
                            <!-- <survey-question
                            v-for="question in subtopic.questions"
                            :key="question.id"
                            :question="question"
                            :answer="0"
                            :readonly="true"
                        > {{question.key}}</survey-question> -->
                        </div>
                    </div>
                </div>
            </div>
            <div v-else>
                <h1>Indicators of the method TBC</h1>
            </div>
            <Button label="Go to surveys" class="p-button-success p-mt-4" style="width: 100%" @click="goToSurveys"/>
        </div>
    </div>

<!-- <div class="p-d-flex p-jc-center">
    <div>
        <div class="p-grid nested-grid" style="width: 1000px">
                  <h1 class="p-col-12">{{method.name}}</h1>
        {{method}}
            <div class="p-col-12">
                {{method.ispublic}} {{method.name}} {{method.description}} {{surveys}}
            </div>
        <Divider />
            <div class="p-col-12" v-for="topic in topics" :key="topic.id">

                <div v-if="topic.parent_topic === null" class="p-shadow-5 p-m-2 p-p-5">
                    Topic: {{topic.name}}
                    <Divider />
                    <div class="p-col-12" v-for="subtopic in topics" :key="subtopic.id">
                        <div v-if="subtopic.parent_topic === topic.id">
                         Topic: {{subtopic.name}}
                    <Divider />
                    <div v-for="question in subtopic.questions" :key="question.id">
                        <p class="p-text-left">Question: {{question.name}}</p>
                        <div v-if="question.options > 0"><h3>options</h3>
                            <div v-for="option in question.options" :key="option.id">
                                <div class="p-shadow-2 p-p-3 p-m-2">{{option.text}}</div>
                            </div>
                        </div>
                    </div>
                    </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div> -->
</template>

<script>
import { mapState, mapActions } from 'vuex'
// import SurveyQuestion from '../../components/survey/SurveyQuestion'
export default {
    // components: {
    //     SurveyQuestion
    // },
    data () {
        return {
            amountDisplayButtonValue: { name: 'Surveys', value: 1 },
            amountDisplayButtonOptions: [
                { name: 'Surveys', value: 1 },
                { name: 'Indicators', value: 0 }
                ]
        }
    },
    computed: {
        ...mapState('method', ['method']),
        ...mapState('topic', ['topics'])
    },
    created () {
        this.initialize()
    },
    methods: {
        ...mapActions('method', ['fetchMethod']),
        ...mapActions('topic', ['fetchTopics']),
        async initialize () {
            await this.fetchMethod({ id: this.method?.id || 0 })
            await this.fetchTopics({ mId: this.method.id })
        }
        // goToSurveys () {
        //     this.$router.push({ name: 'methodsurveys', params: { id: this.method.id } })
        // }
    }

}
</script>
