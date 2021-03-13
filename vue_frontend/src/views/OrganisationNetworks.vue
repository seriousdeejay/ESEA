<template>
<div class="p-grid" style="height: 90vh;">
    <organisation-menu></organisation-menu>
    <div class="p-col">
        <h1 class="p-text-left">Networks</h1>
        <my-networks v-if="!surveys" :query="`?organisation=${this.$route.params.id}`"></my-networks>
        <div v-else class="p-text-italic">
            Your organisation is not participating in any networks.<br> Join a network!
        </div>
    </div>
    </div>
</template>

<script>
import MyNetworks from '../components/MyNetworks'
import OrganisationMenu from '../components/OrganisationMenu'

export default {
    components: {
        MyNetworks,
        OrganisationMenu
    }
}
</script>
