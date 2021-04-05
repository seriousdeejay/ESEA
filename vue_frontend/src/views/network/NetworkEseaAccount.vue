<template>
    <div v-for="value, key in eseaAccount.response_rate" :key="key" class="p-m-5">
            <ProgressBar :value="value.rate + 1" :showValue="true">
                '{{key}}' - Response Rate: {{value.rate}}%
            </ProgressBar>
            <Divider />
            <ProgressBar :value="value.rate + 30" :showValue="true">
                '{{key}}' - Response Rate: {{value.rate + 30}}%
            </ProgressBar>
    </div>

    <div>Esea Account</div>
    {{eseaAccount}}
    <TabView>
        <TabPanel header="Responses">
            <DataTable :value="eseaAccount" datakey="id" :rows="10" :paginator="true" :rowHover="true" selectionMode="single" @row-select="goToSummarizedResponses">
                <template #header>
                    <div class="p-d-flex p-jc-between p-ai-center">
                        <h5 class="p-m-0">Survey Responses</h5>
                        <span class="p-input-icon-left">
                            <i class="pi pi-search" />
                            <InputText v-model="filters" placeholder="Keyword Search" />
                        </span>
                    </div>
                </template>
                <Column field="survey" header="Survey" />
                <!-- <Column field="stakeholdergroup" header="Stakeholder Group"
                <Column field="sufficient_responses" header="Sufficient Responses" />
                <Column field="responses" header="Responses" />
                <Column field="response_rate" header="Response Rate" /> -->
            </DataTable>

        </TabPanel>
        <TabPanel header="Settings">

        </TabPanel>
    </TabView>

</template>

<script>
import { mapState } from 'vuex'
import ProgressBar from 'primevue/progressbar'

export default {
    components: {
        ProgressBar
    },
    data () {
        return {

        }
    },
    computed: {
        ...mapState('eseaAccount', ['eseaAccount'])
    },
    methods: {
        goToSummarizedResponses (event) {
            this.$router.push({ name: 'method-survey-results', params: { OrganisationId: 1, methodId: 1, surveyId: 1 } })
        }
    }
}
</script>

<style type="text/css">
/* .p-progressbar {
background: #f42020;
} */
.memory-bar-style .ui-progressbar-value {
background: #ffe600;
}
.cpu-bar-style .ui-progressbar-value {
background: #7fb80e;
}
</style>
