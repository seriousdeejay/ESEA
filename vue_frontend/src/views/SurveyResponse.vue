<template>
<div class="p-d-flex p-grid p-jc-center">
    <div class="p-col-12">
        <h1>{{survey.name}}</h1>
        <h3>{{survey.description}}</h3>
    </div>
    <Divider />
    <div class="p-col-6">
        <div v-for="subtopic in survey.topics[0].sub_topics" :key="subtopic.id">
        <div v-for="question in subtopic.questions" :key="question.id">
            {{question}}
        </div>
        <br>
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
export default {
    data () {
    },
    computed: {
        ...mapState('method', ['method']),
        ...mapState('survey', ['survey'])
    },
    created () {
        this.initialize()
    },
    methods: {
        ...mapActions('survey', ['fetchSurvey']),
        async initialize () {
            await this.fetchSurvey({ mId: this.method.id, id: this.survey.id })
        }
    }
}
</script>
