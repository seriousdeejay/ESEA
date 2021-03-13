<template>
 <div class="p-grid" style="height: 90vh;">
    <organisation-menu></organisation-menu>
    <div class="p-col">
        <h1 class="p-text-left">Stakeholders</h1>
        <div v-if="!stakeholders">
            <my-users></my-users>
        </div>
        <div v-else class="p-text-italic">
            Your organisation has no stakeholders to display.<br>
        </div>
    </div>
</div>
</template>

<script>
import MyUsers from '../components/MyUsers'
import OrganisationMenu from '../components/OrganisationMenu'

export default {
    components: {
        MyUsers,
        OrganisationMenu
    }
}
</script>
