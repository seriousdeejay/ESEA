<template>
    <div v-if="!stakeholders">
        <my-users :query="`?organisation=${this.$route.params.OrganisationId}`" selection-enabled></my-users>
    </div>
    <div v-else class="p-text-italic">
        Your organisation has no stakeholders to display.<br>
    </div>
</template>

<script>
import MyUsers from '../../components/MyUsers'

export default {
    components: {
        MyUsers
    }
}
</script>
