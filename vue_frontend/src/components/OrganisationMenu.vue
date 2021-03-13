<template>
    <Button icon="pi pi-angle-right" class="p-button-text p-m-2" @click="visibleleft = true" style="background-color: #EFEEEE;"/>
    <Sidebar v-model:visible="visibleleft" style="width:250px;">
        <div class="p-py-5">
            <h3>{{organisation.name}}</h3>
            <Divider />
            <div class="p-d-flex p-flex-column p-px-5">
                <Button label="Overview" icon="pi pi-home" class="p-button-secondary p-button-text" @click="goToOverview" />
                <Button label="Reports" icon="pi pi-chart-bar" class="p-button-secondary p-button-text" @click="goToReports" />
                <Button label="Surveys" icon="pi pi-book" class="p-button-secondary p-button-text" @click="goToSurveys" />
                <Button label="Stakeholders" icon="pi pi-users" class="p-button-secondary p-button-text" @click="goToStakeholders" />
                <Button label="Networks" icon="pi pi-cloud" class="p-button-secondary p-button-text" @click="goToNetworks" />
            </div>
        </div>
    </Sidebar>
</template>

<script>
import { mapState } from 'vuex'
export default {
    data () {
        return {
            visibleleft: false
        }
    },
    computed: {
        ...mapState('organisation', ['organisation'])
    },
    methods: {
        goToOverview () {
            this.$router.push({ name: 'organisationdetails', params: { id: this.organisation?.id || 0 } })
        },
        goToReports () {
            this.$router.push({ name: 'organisationreports', params: { id: this.organisation?.id || 0 } })
        },
        goToSurveys () {
            this.$router.push({ name: 'organisationsurveys', params: { id: this.organisation?.id || 0 } })
        },
        goToStakeholders () {
            this.$router.push({ name: 'organisationstakeholders', params: { id: this.organisation?.id || 0 } })
        },
        goToNetworks () {
            this.$router.push({ name: 'organisationnetworks', params: { id: this.organisation?.id || 0 } })
        }
    }
}
</script>
