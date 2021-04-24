<template>
<div>
    <h2>Indicator Libary</h2>
    <div v-if="items.length">
    <Tree :value="items" v-model:selectionKeys="selectedKey1" selectionMode="single" :expandedKeys="expandedKeys" @nodeSelect="activateItem" style="border-top: 3px solid lightgrey;" />
    <!-- <TreeSelect /> -->
    </div>
    <div v-else> No components to display!</div>
    <!-- {{selectedKey1}}
    {{items}} -->
</div>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'
import getMethodItems from '../utils/getMethodItems'
import Tree from 'primevue/tree'
// import TreeSelect from 'primevue/treeselect'

export default {
    components: {
        Tree
        // TreeSelect
    },
    data () {
        return {
            selectedKey1: null,
            expandedKeys: {}
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

            for (const topic of data) {
                topic.label = topic.name
                for (const subtopic of topic.children) {
                    subtopic.label = subtopic.name
                    for (const indicator of subtopic.children) {
                        indicator.label = indicator.key
                        if (indicator.objType === 'calculation') {
                            indicator.icon = 'pi pi-percentage'
                        } else {
                            indicator.icon = 'pi pi-pencil'
                        }
                    }
                }
            }
            return data
            // const arr = []
            // console.log('::', data)
            // data.forEach(el => console.log(el)) // arr.push({ label: el.name, key: el.name }))
            // return arr
            // return arr
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
    mounted () {
        this.expandAll()
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
        },
        expandAll () {
            for (const node of this.items) {
                this.expandNode(node)
            }

            this.expandedKeys = { ...this.expandedKeys }
        },
        expandNode (node) {
            this.expandedKeys[node.key] = true
            if (node.children && node.children.length) {
                for (const child of node.children) {
                    this.expandNode(child)
                }
            }
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
