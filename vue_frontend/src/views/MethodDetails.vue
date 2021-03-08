<template>
<div class="p-d-flex p-jc-center">
    <div><h1>{{method.name}}</h1></div>
    <div>eeee</div>
    <div>
        {{method}}
        <Divider />
        <div class="p-grid nested-grid" style="width: 1000px">
            <div class="p-col-12" v-for="topic in topics" :key="topic.id">
                <div class="p-shadow-5 p-m-2 p-p-5">
                    Topic: {{topic.name}}
                    <Divider />
                    <div v-for="question in topic.questions" :key="question.id">
                        <p class="p-text-left">Question: {{question.name}}</p>
                        <Divider />
                        <div v-if="question.options.length > 0"><h3>options</h3>
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
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
    data () {
        return {
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
    }

}
</script>
