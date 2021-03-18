<template>

<div class="p-grid nested-grid p-px-2" style="min-height: 60vh;">
    <div class="p-col-9">
        <div class="p-col-12 p-text-justify"><h4 class="p-text-bold">Description</h4>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. In convallis mi sit amet faucibus malesuada. Vestibulum fringilla sed dui bibendum laoreet. Donec suscipit sit amet leo et mattis. Aenean mattis tempus turpis a vulputate. Nunc bibendum pulvinar neque, nec mattis nisl tincidunt ut. Nam a quam id justo dictum pulvinar. Sed luctus dictum ligula, id sagittis tellus aliquam id. Vestibulum auctor vestibulum turpis.
        </div>
         <div class="p-col-12 p-p-5 p-m-5" style="border: 1px solid lightgray; background-color: white; border-radius: 5px;">
            <div v-if="Tasks">
                <h4>No tasks!</h4>
                <p class="p-text-italic">
                    {{network.name}} does not require your attention right now.
                </p>
            </div>
            <div v-else>
                <h4 class="p-mb-0">The following tasks require your attention.</h4>
                <div v-for="survey, index in surveys" :key="survey.id" class="p-p-5">
                    <Button :label="`Survey ${index+1}: As ${survey.stakeholders} of ${organisation.name} you are asked to fill in the following survey deployed by network 1: '${survey.name}'.`" class="p-button-text p-shadow-3 p-p-4" @click="goToSurvey(survey.method.id, survey.id)"/>
                    <br><br>
                    <Button label="Task 2: As manager of organisation 2 you are asked to fill in the survey of network 1." class="p-button-text p-shadow-1" />
                </div>
                <br>
                <Button label="Task 1: Organisation is requesting network membership." class="p-button-secondary p-shadow-1" />
                <br><br>
                <Button label="Task 2: Survey responserate threshold has been achieved for method BIA." class="p-button-secondary p-shadow-1" />
            </div>
        </div>
    </div>
    <div class="p-col-1">
        <Divider layout="vertical"></Divider>
    </div>
    <div class="p-col-2">
        <div class="p-grid">
            Content here
             <!-- <div class="p-col-12">
                <h3 class="p-mb-2 p-text-left">Available Surveys</h3>
                <Divider class="p-m-0" />
                <div class="p-m-3">
                    <div v-if="surveys.length">
                        <div v-for="survey, num in surveys" :key="survey.name">
                            {{num+1}}. <router-link :to="{name: 'survey-fill', params: { id: survey.method.id, surveyId: survey.id }}" style="text-decoration: none; color: blue;">survey {{num+1}}</router-link>
                            <Divider class="p-m-1" />
                        </div>
                    </div>
                    <div v-else>
                        <div class="p-py-5 p-text-italic">No surveys</div>
                    </div>
                </div>
                <router-link :to="{name: 'organisationsurveys', params: { OrganisationId: this.$route.params.OrganisationId }}" style="text-decoration: none; color: blue;">Show all Organisation Surveys</router-link>
            </div>
            <div class="p-col-12">
                <h3 class="p-mb-2 p-text-left">Reports</h3>
                <Divider class="p-m-0" />
                <div class="p-m-3">
                    <div v-if="organisations">
                        <div v-for="organisation, num in organisations" :key="organisation.name">
                            {{num+1}}. <router-link :to="{name: 'organisationreports', params: { OrganisationId: this.$route.params.OrganisationId }}" style="text-decoration: none; color: blue;">report {{num+1}}</router-link>
                            <Divider class="p-m-1" />
                        </div>
                    </div>
                    <div v-else>
                        <div class="p-py-5 p-text-italic">No reports yet</div>
                    </div>
                </div>
                <router-link :to="{name: 'organisationreports', params: { OrganisationId: this.$route.params.OrganisationId } }" style="text-decoration: none; color: blue;">Show all Organisation Reports</router-link>
            </div> -->
        </div>
    </div>
</div>
</template>
<script>
import { mapActions, mapState } from 'vuex'
export default {
    computed: {
        ...mapState('network', ['network']),
        ...mapState('method', ['methods']),
        ...mapState('survey', ['surveys'])
    },
    created () {
        // this.initialize()
    },
    methods: {
        ...mapActions('method', ['fetchMethods']),
        ...mapActions('survey', ['fetchSurveys'])
        // async initialize () {
        //     await this.fetchMethods({})
        //     for (const method of this.methods) {
        //         await this.fetchSurveys({ mId: method.id, query: `?organisation=${this.$route.params.OrganisationId}` })
        //     }
        // }
    }
}
</script>
