<template>
    <div class="p-d-flex p-jc-center">
        <div>
            <div class="p-d-flex p-jc-center">
                <div><h1> {{user.username}}'s Profile</h1>
                {{currentuser.username}} {{user.username}}</div>
            </div>
        <div class="card p-px-5">
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
                        <div class="p-col-6"> {{ user.date_joined.slice(0, 10) }} </div> <!-- Date should be fixed to DD-MM-YYYY! -->
                        <div class="p-col-12" >
                            <div class="p-text-bold" >Bio</div>
                            <p class="p-text-justify">Hello this is my Bio! Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
                        </div>
                    </div>
                </div>
                <div class="p-col-1"></div>
                <img class="p-shadow-5" :src="user.image" alt="Profile Avatar" style="max-width: 200px; max-height: 200px; border-radius: 50%;" format="PNG">
                <!-- <div class="p-col-4 p-shadow-1" style="border-style: solid; border-color: #f2f2f2; border-width: thin; opacity: 0.6"> -->
            </div>
            <Divider />
            <div v-if="currentuser === user.username" class="p-d-flex p-jc-start">
                <Button label="Edit Profile" class="p-button-raised p-button-primary p-mr-2" @click="editProfile" />
                <Button label="Delete Account" class="p-button-raised p-button-danger" @click="(deleteAccountDialog = true)" /> <!-- If user profile belongs to logged in user-->
            </div>
        </div>
        </div>
    </div>

    <Dialog v-if="user" v-model:visible="deleteAccountDialog" :style="{width: '450px'}" header="Confirm" :modal="true">
        <div class="confirmation-content">
            <i class="pi pi-exclamation-triangle p-mr-3" style="font-size:1.5rem" />
            <span>Are you sure you want to delete the following account: '<b>{{user.username}}</b>'?</span>
        </div>
        <template #footer>
            <Button label="No" icon="pi pi-times" class="p-button-text" @click="deleteAccountDialog = false"/>
            <Button label="Yes" icon="pi pi-check" class="p-button-text" @click="deleteAccount()" />
        </template>
    </Dialog>

</template>

<script>
// import store from '../store'
import { mapActions, mapState } from 'vuex'

export default {
    data () {
        return {
            deleteAccountDialog: false

        }
    },
    computed: {
        ...mapState('user', ['user']),
        ...mapState('authentication', ['currentuser', 'authenticatedUser'])
    },
    methods: {
        ...mapActions('user', ['updateUser', 'deleteUser']),
        editProfile () {
            console.log('e')
            // this updateUser({})
        },
        async deleteAccount () {
            if (this.currentuser === this.user.username) {
                // await this.deleteUser({ ...this.user })
                this.$router.push({ name: 'logout' })
            }
        }
    }
}
</script>
