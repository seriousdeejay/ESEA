<template>
    <div class="p-grid" style="height: 100vh;">
        <div class="p-col-fixed" style="width: 50px;">
            <organisation-sidebar @page="changePagename" />
        </div>
        <div class="p-col">
            <div class="p-col-12 p-text-left p-text-italic p-m-0">
                <p>{{organisation.name}}</p>
                <h3>{{currentPage}}</h3>
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
        currentPage: ''
        }
    },
    computed: {
        ...mapState('organisation', ['organisation'])
    },
    methods: {
        changePagename (pagename) {
            console.log(pagename)
            this.currentPage = pagename
        }
    }
}
</script>
