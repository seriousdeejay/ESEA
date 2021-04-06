<template>
    <Button label="New Campaign" icon="pi pi-plus" class="p-button-success p-d-flex p-mx-5" @click="createCampaignDialog = true" />
    <Divider />
    <div class="p-grid p-m-5">
        <div v-for="eseaAccount in eseaAccounts" :key="eseaAccount.id" class="p-col-12 p-md-6 p-lg-4" style="width: 450px">
            <div class="p-p-3" :class="eseaAccount.hover ? 'p-shadow-10 p-m-1' : 'p-shadow-5 p-m-2'" style="border-radius: 3px" :style="(eseaAccount.hover ? styleObject : '')"
            @mouseover="eseaAccount.hover=true" @mouseleave="eseaAccount.hover = false" @click="goToEseaAccount(eseaAccount)">
                <h3>campaign: {{ eseaAccount.campaign }}</h3>
                <Divider />
                <div class="p-text-left p-ml-5">
                    <div class="p-grid">
                        <p class="p-col-6">Method: <span class="p-text-bold">{{eseaAccount.method.name}}</span></p>
                        <p class="p-col-6"> Report: <span class="p-text-bold">{{eseaAccount.report}} No</span></p>
                        <p class="p-col-6">Respondents: <span class="p-text-bold">{{eseaAccount.all_respondents}}</span></p>
                        <p class="p-col-6">Responses: <span class="p-text-bold">{{eseaAccount.all_responses.length}}</span></p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { mapActions, mapState } from 'vuex'
export default {
    data () {
        return {
            hover: false,
            styleObject: { backgroundColor: '#EFEEEE' }
        }
    },
    computed: {
        ...mapState('eseaAccount', ['eseaAccounts'])
    },
    created () {
        this.initialize()
    },
    methods: {
        ...mapActions('eseaAccount', ['fetchEseaAccounts', 'setEseaAccount']),
        async initialize () {
            await this.fetchEseaAccounts({ nId: 0, cId: 0, query: `?organisation=${this.$route.params.OrganisationId}` })
        },
        async goToEseaAccount (eseaAccount) {
            await this.setEseaAccount(eseaAccount)
            this.$router.push({ name: 'organisationeseaaccount', params: { EseaAccountId: eseaAccount.id } })
        }
    }
}
</script>
