<template>
<h1>dd</h1>
    <div class="card p-mx-5 p-mb-5">
        a
        <!-- <div class="p-d-flex p-jc-between p-m-2">
            <div>
                {{ dateFixer(campaign.open_survey_date, 'MMMM Do YYYY') }}
            </div>
            <div>
                {{ dateFixer(campaign.close_survey_date, 'MMMM Do YYYY') }}
            </div>
        </div>
        <ProgressBar :value="timeline" :showValue="true">
            <div v-if="campaigntimeleft > 0"> {{campaigntimeleft}} days left </div>
            <div v-else>This campaign has finished</div>
        </ProgressBar> -->
    </div>
    {{eseaAccount}}
</template>

<script>
import { mapState } from 'vuex'
// import ProgressBar from 'primevue/progressbar'

export default {
    components: {
        // ProgressBar
    },
    data () {
        return {
        }
    },
    computed: {
        ...mapState('eseaAccount', ['eseaAccount'])
    }
}
</script>
