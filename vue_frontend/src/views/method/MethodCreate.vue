<template>

<div class="p-grid p-m-0" style="background-color: white;">
    <method-tree-sidebar class="p-col-fixed" style="width: 300px; border-right: 1px solid lightgrey;"/>
    <div class="p-col p-m-5 p-p-5 p-text-left p-shadow-5">
        <method-form :method="method" @input="updateMethod($event)" />
        <Divider />
        <div v-for="(topic, topicIndex) in items" :key="`topic-${topicIndex}`" class="p-shadow-2 p-pb-5" style="background-color: #f7f7f7;">
            <topic-form ref="items" :topic="topic" :active="activeItem.objType === topic.objType && activeItem.id === topic.id" @input="saveActive('topic', $event)" @click="toggleActive(topic)" /> <!-- @click.native="toggleActive(topic)" -->
            <div v-for="(topicChild, index) in topic.children" :key="`topicChild-${index}`" >
                <div class=" p-m-5" style="border: 1px solid lightgrey; background-color: white;">
                <component :is="`${topicChild.objType}-form`" ref="items" :topic="topicChild" :question="topicChild" :errors="errors[topicChild.objType] && errors[topicChild.objType][topicChild.id]" :indirect-indicator="topicChild" :active="activeItem.objType === topicChild.objType && activeItem.id === topicChild.id" @input="saveActive(topicChild.objType, $event)" @click="toggleActive(topicChild)" />
                <div v-for="(subTopicChild, index) in topicChild.children" :key="`subTopicChild-${index}`">
                    <component :is="`${subTopicChild.objType}-form`" ref="items" :topic="subTopicChild" :question="subTopicChild" :indirect-indicator="subTopicChild" :errors="errors[subTopicChild.objType] && errors[subTopicChild.objType][subTopicChild.id]" :active="activeItem.objType === subTopicChild.objType && activeItem.id === subTopicChild.id" @input="saveActive(subTopicChild.objType, $event)" @click="toggleActive(subTopicChild)"  class="p-my-5 p-mx-5" />
                </div>
                </div>
            </div>
        </div>
        <Button label="Add New Topic" icon="pi pi-plus" class="p-button-text" @click="addTopic" />
    </div>
    <!-- <question-form :question="activeQuestion" :active="true" /> -->
    <div class="p-col-fixed p-d-flex p-ai-center" style="width: 150px; border: 1px solid lightgrey;">
        <div>
            <div v-for="option in addBar" :key="option.choice" class="p-d-flex p-jc-center p-ai-center" style="height: 100px; width: 100px; border: 1px solid lightgrey" :style="(option.hover ? 'background-color: lightgrey;' : '')" @mouseover="option.hover=true" @mouseleave="option.hover=false" @click="addBarMethod(option.choice)">
                <div>
                    <i :class="option.icon? option.icon : 'pi pi-plus'" />
                    <p class="p-text-italic p-m-2">{{option.choice}}</p>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- Method creation wizard -->
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'
import MethodTreeSidebar from '../../components/MethodTreeSideBar'
import MethodForm from '../../components/forms/MethodForm'
import TopicForm from '../../components/forms/TopicForm'
import QuestionForm from '../../components/forms/QuestionForm'
import CalculationForm from '../../components/forms/CalculationForm'
import getMethodItems from '../../utils/getMethodItems'

export default {
    components: {
        MethodTreeSidebar,
        MethodForm,
        TopicForm,
        QuestionForm,
        CalculationForm
    },
    data () {
        return {
            updateToolbar: 0,
            addBar: [
                { choice: 'question' },
                { choice: 'subtopic' },
                { choice: 'calculation' },
                { choice: 'delete', icon: 'pi pi-trash' }
            ]
        }
    },
    computed: {
        ...mapState('method', ['method', 'error']),
        ...mapState('topic', { topics: 'topics', activeTopic: 'topic', topicErrors: 'errors' }),
        ...mapGetters('topic', ['methodTopics', 'subTopics']),
        ...mapState('question', { activeQuestion: 'question', questionErrors: 'errors' }),
        ...mapGetters('question', ['topicQuestions']),
        ...mapState('indirectIndicator', { activeIndirectIndicator: 'indirectIndicator', indirectIndicatorErrors: 'errors' }),
        ...mapGetters('indirectIndicator', ['topicIndirectIndicators']),
        items () {
            return getMethodItems(
                this.methodTopics,
                this.subTopics,
                this.topicQuestions,
                this.topicIndirectIndicators
            )
        },
        activeItem () {
            let objType = 'topic'
            let { id } = this.activeTopic

            if (this.activeQuestion.id) {
                objType = 'question'
                id = this.activeQuestion.id
            }
            if (this.activeIndirectIndicator.id) {
                objType = 'calculation'
                id = this.activeIndirectIndicator.id
            }
            return { objType, id }
        },
        errors () {
            return {
                question: this.questionErrors,
                topic: this.topicErrors,
                calculation: this.indirectIndicatorErrors
            }
        }
    },
    created () {
        this.initialize()
    },
    methods: {
        ...mapActions('method', ['fetchMethod', 'updateMethod', 'saveMethod']),
        ...mapActions('topic', ['fetchTopics', 'setTopic', 'updateTopic', 'addNewTopic', 'deleteTopic']),
        ...mapActions('question', ['fetchQuestions', 'setQuestion', 'addNewQuestion', 'deleteQuestion', 'updateQuestion']),
        ...mapActions('indirectIndicator', ['fetchIndirectIndicators', 'addNewIndirectIndicator', 'updateIndirectIndicator', 'setIndirectIndicator', 'deleteIndirectIndicator']),
        async initialize () {
            const methodId = parseInt(this.$route.params.id, 10)
            if (this.method.id !== methodId) {
                await this.fetchMethod({ id: methodId })
                if (this.error) {
                    this.$router.push({ name: 'methods' })
                }
            }
            await this.fetchTopics({ mId: this.method.id })
            await this.fetchQuestions({ mId: this.method.id })
            await this.fetchIndirectIndicators({ mId: this.method.id })
            // this.toggleActive({ objType: 'topic' })
        },
        addTopic () {
            this.addNewTopic()
            this.setQuestion()
            this.setIndirectIndicator()
        },
        addSubTopic () {
            this.addNewTopic({ parent: this.activeTopic.parent_topic || this.activeTopic.id })
            this.setQuestion()
            this.setIndirectIndicator()
        },
        addQuestion () {
            this.addNewQuestion({ topic: this.activeTopic.id })
            this.setIndirectIndicator()
        },
        addIndirectIndicator () {
            this.addNewIndirectIndicator({ topic: this.activeTopic.id })
            this.setQuestion()
        },
        toggleActive (item) {
            const { objType } = item
            const topic = { id: item.topic || item.id }
            this.setTopic(topic)
            if (objType === 'topic') {
                this.setQuestion()
                this.setIndirectIndicator()
            } else if (objType === 'question' && item.id !== this.activeQuestion.id) {
                this.setQuestion(item)
                this.setIndirectIndicator()
            } else if (objType === 'calculation' && item.id !== this.activeIndirectIndicator.id) {
                this.setIndirectIndicator(item)
                this.setQuestion()
            }
        },
        saveActive (type, object) {
            console.log('!!', 'type:', type, 'object:', object)
            if (type === 'topic') {
                this.updateTopic({
                    mId: this.method.id,
                    topic: object
                })
            }
            if (type === 'question') {
                if (object.key) {
                this.updateQuestion({
                    mId: this.method.id,
                    question: object
                })
                }
            }
            if (type === 'calculation') {
                this.updateIndirectIndicator({
                    mId: this.method.id,
                    indirectIndicator: object
                })
            }
        },
        deleteActive () {
            const objType = this.activeItem.objType
            const id = this.activeItem.id
            // const { objType, id } = this.activeitem
            if (objType === 'topic') {
                this.deleteTopic({ mId: this.method.id, id })
            }
            if (objType === 'question') {
                this.deleteQuestion({ mId: this.method.id, id })
            }
            if (objType === 'calculation') {
                this.deleteIndirectIndicator({ mId: this.method.id, id })
            }
        },
        addBarMethod (choice) {
            if (choice === 'question') { this.addQuestion() }
            if (choice === 'subtopic') { this.addSubTopic() }
            if (choice === 'calculation') { this.addIndirectIndicator() }
            if (choice === 'delete') { this.deleteActive() }
        }
    }
}
</script>

<style lang="scss" scoped>
.p-divider {
    background-color: white;
}
</style>
