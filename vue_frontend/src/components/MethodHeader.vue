<template>
    <div class="p-d-flex p-ai-center p-jc-between p-px-5" style="height: 80px; background-color: #f1f1f1;">
        <div class="p-d-flex p-ai-center">
            <i class="pi pi-arrow-left p-px-5" style="font-size: 30px;" @click="goToMethods()"></i>
            <h2>{{ title }} <span class="p-text-italic p-text-light p-ml-5"><small><template v-if="upToDate">All changes saved</template><template v-else>...</template></small></span></h2>
        </div>
        <div class="p-d-flex p-ai-center" style="height: 100%;">
        <div v-for="step in steps" :key="step.text" class="p-d-flex p-ai-center" @mouseover="step.hover = true" @mouseleave="step.hover = false" :style="(step.hover ? styleObject : '')" style="height: 100%;">
            <div class="p-text-light p-p-5" @click="goToPage(step.to)"  style="text-align: center;">{{step.text}}</div>
        </div>
        </div>

    </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
    data () {
        return {
        steps: [
            { text: 'Design Method', to: { name: 'method-create' } },
            { text: 'Survey Creation', to: { name: 'survey-create' } }
            ],
        styleObject: { 'background-color': 'skyblue' }
        }
    },
    computed: {
        ...mapState('method', ['method']),
		...mapState('topic', { topicsSaved: 'isSaved' }),
		...mapState('question', { questionsSaved: 'isSaved' }),
		...mapState('indirectIndicator', { IndirectIndicatorsSaved: 'isSaved' }),
		// ...mapState('survey', { SurveysSaved: 'isSaved' }),
        title () {
            return this.method.id ? this.method.name : 'New Method'
        },
        updToDate () {
            const all = {
                ...this.topicsSaved,
                ...this.questionsSaved,
                ...this.IndirectIndicatorsSaved
                // ...this.SurveysSaved,
            }
            const found = Object.values(all).find(value => value === false)
            return found === undefined
        }
    },
    methods: {
        goToMethods () {
            this.$route.push({ name: 'methods' })
        },
        goToPage (page) {
            page.params = { id: this.$route.params.id }
            this.$router.push(page)
        }
    }
}
</script>
