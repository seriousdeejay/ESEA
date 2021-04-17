<template>
<div>
    <h3 class="p-text-left">Indicator Libary</h3>
    <Divider />
    <Tree :value="items" v-model:selectionKeys="selectedKey1" selectionMode="single" @nodeSelect="activateItem" />
    <!-- {{selectedKey1}}
    {{items}} -->
</div>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'
import getMethodItems from '../utils/getMethodItems'
import Tree from 'primevue/tree'

export default {
    components: {
        Tree
    },
    data () {
        return {
            selectedKey1: null
        }
    },
    computed: {
        ...mapState('method', ['method']),
        ...mapState('topic', { activeTopic: 'topic' }),
        ...mapState('question', { activeQuestion: 'question' }),
		...mapState('indirectIndicator', { activeIndirectIndicator: 'indirectIndicator' }),

        ...mapGetters('topic', ['methodTopics', 'subTopics']),
		...mapGetters('question', { topicQuestions: 'topicQuestions' }),
		...mapGetters('indirectIndicator', ['topicIndirectIndicators']),
		items () {
            const data = getMethodItems(this.methodTopics,
				this.subTopics,
				this.topicQuestions,
				this.topicIndirectIndicators)
            const arr = []
            data.forEach(el => arr.push({ label: el.name, key: el.name }))
            return arr
			// return getMethodItems(
            //     this.methodTopics,
            //     this.subTopics,
            //     this.topicQuestions,
            //     this.topicIndirectIndicators
			// )
        }
    },
    watch: {
        activeItem () {
            if (this.activeQuestion.id) {
				this.itemsOpen.push(`topic_${this.activeQuestion.topic}`)
			}
			if (this.activeIndirectIndicator.id) {
				this.itemsOpen.push(`topic_${this.activeIndirectIndicator.topic}`)
			}
			if (this.activeTopic.parent_topic) {
				this.itemsOpen.push(`topic_${this.activeTopic.parent_topic}`)
			}
        }
    },
    methods: {
        ...mapActions('topic', ['setTopic']),
		...mapActions('question', ['setQuestion']),
		...mapActions('indirectIndicator', [
			'setIndirectIndicator',
			'updateIndirectIndicator'
		]),
        activateItem (item) {
            console.log('ss', item)
        },
		setActiveItem (active) {
			const [type, id] = active.split('_')
			const parsedId = parseInt(id, 10)
			if (type === 'topic') {
				this.setTopic({ id: parsedId })
				this.setQuestion()
				this.setIndirectIndicator()
			} else if (type === 'question') {
				this.setQuestion({ id: parsedId })
				this.setIndirectIndicator()
			} else if (type === 'calculation') {
				this.setIndirectIndicator({ id: parsedId })
				this.setQuestion()
			}
        },
        addToCalculation (item) {
			this.updateIndirectIndicator({
				mId: this.method.id,
				indirectIndicator: {
					...this.activeIndirectIndicator,
					formula: `${this.activeIndirectIndicator.formula} [${item.key}]`
				}
			})
        }
    }
}
</script>

<style lang="scss" scoped>
.p-tree {
    background: none;
    border: 1px solid lightgray;
}
</style>
