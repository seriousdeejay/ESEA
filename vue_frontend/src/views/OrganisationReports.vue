<template>
 <div class="p-grid" style="height: 90vh;">
    <organisation-menu></organisation-menu>
    <div class="p-col">
        <h1 class="p-text-left">Reports</h1>
        <div v-if="stakeholders">
            <my-reports></my-reports>
        </div>
        <div v-else class="p-text-italic">
            Your organisation has no reports to display.<br> Join a network and fill in surveys to get reports!
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
