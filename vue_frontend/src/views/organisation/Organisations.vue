<template>
    <my-organisations2 />
    <div class="organisations">
        <h1>Organisations Overview</h1>
        <Toast position="top-right"/>
        <div class="card p-m-5 p-shadow-2">
            <my-organisations selection-enabled></my-organisations>
        </div>
    </div>
</template>

<script>
import MyOrganisations from '../../components/MyOrganisations'
import MyOrganisations2 from '../../components/MyOrganisationsV2'

export default {
    components: {
       MyOrganisations,
       MyOrganisations2
    },
    data () {
        return {
        }
    }
}
</script>
