<template>
    <Button icon="pi pi-angle-right" class="p-button-text" @click="visibleleft = true" style="background-color: #EFEEEE; height: 100%;"/>
    <Sidebar v-model:visible="visibleleft" style="width:250px;">
        <div class="p-py-5">
            <h3>{{organisation.name}}</h3>
            <Divider />
            <div class="p-d-flex p-flex-column p-px-5 p-text-left">
                <div v-for="link in links" :key="link.label">
                    <Button :label="link.label" :icon="`pi pi-${link.icon}`" class="p-button-secondary p-button-text" @click="goToPage(link.label)" />
                </div>
            </div>
        </div>
    </Sidebar>
</template>

<script>
import { mapState } from 'vuex'
export default {
    data () {
        return {
            visibleleft: false,
            links: [
                { label: 'Overview', icon: 'home' },
                { label: 'Reports', icon: 'chart-bar' },
                { label: 'Surveys', icon: 'book' },
                { label: 'Stakeholders', icon: 'users' },
                { label: 'Networks', icon: 'cloud' }
            ],
            name: ''
        }
    },
    computed: {
        ...mapState('organisation', ['organisation'])
    },
    watch: {
        '$route' () {
        this.$emit('page', this.name)
        }
    },
    methods: {
        goToPage (name) {
            this.name = name
            name = name.toLowerCase()
            this.$router.push({ name: `organisation${name}`, params: { OrganisationId: this.organisation?.id || 0 } })
        }
    }
}
</script>
