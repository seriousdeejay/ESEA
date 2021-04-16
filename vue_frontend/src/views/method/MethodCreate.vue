<template>
<div class="p-grid p-mt-5">
    <div class="p-fixed" style="width: 200px">
        {{method}}
    </div>
    <div class="p-col">
        <method-form :method="method" @input="updateMethod($event)" />
    </div>
    <div v-for="(topic, topicIndex) in items" :key="`topic-${topicIndex}`">
        mydiv
        <topic-form ref="items" :topic="topic" :active="activeItem.objType === topic.objType && activeItem.id === topic.id" @input="saveActive('topic', $event)"  /> <!-- @click.native="toggleActive(topic)" -->
    </div>
</div>
<!-- Method creation wizard -->
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'
import MethodForm from '../../components/forms/MethodForm'
import TopicForm from '../../components/forms/TopicForm'
// import QuestionForm from '../../components/forms/QuestionForm'
// import CalculationForm from '../../components/form/CalculationForm'
import getMethodItems from '../../utils/getMethodItems'

export default {
    components: {
        MethodForm,
        TopicForm
    },
    data () {
        return {
            updateToolbar: 0
        }
    },
    computed: {
        ...mapState('method', ['method', 'error']),
        ...mapState('topic', { topics: 'topics', activeTopic: 'topic', topicErrors: 'errors' }),
        ...mapGetters('topic', ['methodTopics', 'subTopics']),
        // ...mapState('question', { activeQuestion: 'question', questionErrors: 'errors' }),
        // ...mapGetters('question', ['topicQuestions']),
        // ...mapState('indirectIndicator', { activeIndirectIndicator: 'indirectIndicator', indirectIndicatorErrors: 'errors' }),
        // ...mapGetters('indirectIndicator', ['topicIndirectIndicators']),
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
        ...mapActions('topic', ['fetchTopics', 'updateTopic', 'addNewTopic', 'deleteTopic']), // setTopic
        // ...mapActions('question', ['fetchQuestions, setQuestion, addNewQuestion, deleteQuestion, updateQuestion']),
        // ...mapActions('indirectIndicator', ['fetchIndirectIndicators', 'addNewIndirectIndicator', 'updateIndirectIndicator', 'setIndirectIndicator', 'deleteIndirectIndicator']),
        async initialize () {
            const methodId = parseInt(this.$route.params.id, 10)
            if (this.method.id !== methodId) {
                await this.fetchMethod({ id: methodId })
                if (this.error) {
                    this.$router.push({ name: 'methods' })
                }
            }
            await this.fetchTopics({ mId: this.method.id })
            // await this.fetchQuestions({ mId: this.method.id })
            // await this.fetchIndirectIndicators({ mId: this.method.id })
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
        toggleActive (item) {
            // fill in
        },
        saveActive (type, object) {
            // fill in
        },
        deleteActive () {
            // fill in
        }
    }
}
</script>
