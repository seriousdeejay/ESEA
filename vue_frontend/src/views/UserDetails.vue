<template>
    <div class="p-d-flex p-jc-center">
        <div class="card p-px-5">
            <h1> {{user.username}}'s Profile</h1>
            {{currentuser.username}} {{user.username}}
            <Divider />
            <div class="p-grid nested-grid p-p-5" style="width: 1000px">
                <div class="p-col-7 p-text-left p-p-3">
                    <div class="p-grid">
                        <div class="p-col-6 p-text-bold"> Username </div>
                        <div class="p-col-6"> {{ user.username }} </div>
                        <div class="p-col-6 p-text-bold"> Full name </div>
                        <div class="p-col-6 "> {{ `${user.first_name} ${user.last_name}` }} </div>
                        <div class="p-col-6 p-text-bold"> Email </div>
                        <div class="p-col-6"> {{ user.email }} </div>
                        <div class="p-col-6 p-text-bold"> Account Creation </div>
                        <div class="p-col-6"> {{ user.registered_on.slice(0, 10) }} </div> <!-- Date should be fixed to DD-MM-YYYY! -->
                        <div class="p-col-12" >
                            <div class="p-text-bold" >Bio</div>
                            <p class="p-text-justify">Hello this is my Bio! Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
                        </div>
                    </div>
                </div>
                <div class="p-col-1"></div>
                <div class="p-col-4 p-shadow-1" style="border-style: solid; border-color: #f2f2f2; border-width: thin; opacity: 0.6">
                    Avatar here
                </div>
                <div class="p-mt-5">
                </div>
            </div>
            <Divider />
            <div v-if="currentuser === user.username" class="p-d-flex p-jc-start">
                <Button label="Edit Profile" class="p-button-raised p-button-primary" @click="editProfile" /> <!-- If user profile belongs to logged in user-->
            </div>
        </div>
    </div>

</template>

<script>
// import store from '../store'
import { mapState } from 'vuex'

export default {
    data () {
        return {

        }
    },
    computed: {
        ...mapState('user', ['user']),
        ...mapState('authentication', ['currentuser', 'authenticatedUser'])
    },
    methods: {
        editProfile () {
            console.log('e')
        }
    }
}
</script>
