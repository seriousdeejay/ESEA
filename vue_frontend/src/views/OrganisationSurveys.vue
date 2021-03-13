<template>

 <div class="p-grid" style="height: 90vh;">
    <organisation-menu></organisation-menu>
    <div class="p-col">
        <h1 class="p-text-left">Surveys</h1>
        <div v-if="surveys"></div>
        <div v-else class="p-text-italic">
            Your organisation has no surveys to display.<br> Join a network to get available surveys!
        </div>
    </div>
 </div>
</template>

<script>
import OrganisationMenu from '../components/OrganisationMenu'
export default {
    components: {
        OrganisationMenu
    }
}
</script>
