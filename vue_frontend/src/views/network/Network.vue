<template>
    <div class="p-grid" style="height: 100vh">
        <div class="p-col-fixed" style="width: 50px">
            <organisation-sidebar :links="links" :name="network.name" @reroute="goToPage"/>
        </div>
        <div class="p-col">
            <div class="p-col-12 p-text-left p-text-italic p-m-0 p-px-5">
                <p>{{network.name}}</p>
                <h3>{{pagename || this.$route.meta.breadcrumb[this.$route.meta.breadcrumb.length-1].label}}</h3>
            </div>
            <router-view />
        </div>
    </div>
</template>

<script>
import { mapState } from 'vuex'
import OrganisationSidebar from '../../components/OrganisationSidebar'
export default {
    components: {
        OrganisationSidebar
    },
    data () {
        return {
            links: [
                { label: 'Overview', icon: 'home' },
                { label: 'Campaigns', icon: 'chart-bar' },
                { label: 'Methods', icon: 'chart-bar' },
                // { label: 'Stakeholders', icon: 'users' },
                { label: 'Organisations', icon: 'cloud' },
                { label: 'Settings', icon: 'cog' }
            ],
            pagename: undefined
        }
    },
    computed: {
        ...mapState('network', ['network'])
    },
    methods: {
        goToPage (name) {
            this.pagename = name
            this.$router.push({ name: `network${name.toLowerCase()}`, params: { NetworkId: this.network?.id || 0 } })
        }
    }
}
</script>
