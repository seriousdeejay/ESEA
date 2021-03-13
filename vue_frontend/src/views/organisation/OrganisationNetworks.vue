<template>
    <my-networks :query="`?organisation=${this.$route.params.OrganisationId}`" organisation-networks selection-enabled></my-networks>
    <!-- <div class="p-text-italic">
        Your organisation is not participating in any networks.<br> Join a network!
    </div> -->
</template>

<script>
import MyNetworks from '../../components/MyNetworks'

export default {
    components: {
        MyNetworks
    }
}
</script>
