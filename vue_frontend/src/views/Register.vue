<template>
    <div style="width: 30rem; border-radius:0.25rem" class="p-d-block p-mx-auto p-p-5 p-shadow-10">
        <h1>Create An Account</h1>
        <p v-if="incorrectAuth">Incorrect username or password entered - please try again!</p>
        <form v-on:submit.prevent="register">
            <div class="p-field p-grid">
                <label for="username" class="p-col">Username</label>
                <div class="p-col">
                    <InputText type="text" id="username" v-model="customuser.username" />
                </div>
            </div>

            <div class="p-field p-grid">
                <label for="password" class="p-col" >Password</label>
                <div class="p-col">
                    <Password id="password" v-model="customuser.password" :feedback="false" />
                </div>
            </div>

            <div class="p-field p-grid">
                <label for="password2" class="p-col" >Password2</label>
                <div class="p-col">
                    <Password id="password2" v-model="customuser.password2" :feedback="false" />
                </div>
            </div>

            <div class="p-field p-grid">
                <label for="email" class="p-col">Email</label>
                <div class="p-col">
                    <InputText type="text" id="email" v-model="customuser.email" />
                </div>
            </div>

            <div class="p-field p-grid">
                <label for="firstname" class="p-col">First Name</label>
                <div class="p-col">
                    <InputText type="text" id="firstname" v-model="customuser.first_name" />
                </div>
            </div>

            <div class="p-field p-grid">
                <label for="lastnameprefix" class="p-col"> Last Name Prefix</label>
                <div class="p-col">
                    <InputText type="text" id="lastnameprefix" v-model="customuser.last_name_prefix" />
                </div>
            </div>

                      <div class="p-field p-grid">
                <label for="lastname" class="p-col">Last Name</label>
                <div class="p-col">
                    <InputText type="text" id="lastname" v-model="customuser.last_name" />
                </div>
            </div>

            <div style="text-align:right">
                <Button type="submit" value="submit">Register Account</Button>
            </div>
        </form>
        <br>
        <hr>
        <div class="p-d-flex p-jc-between p-ai-center">
            <h4>Already have an Account?</h4>
            <div>
            <Button @click="$router.push('login')" class="p-button-secondary">Go to Login</Button>
        </div>
        </div>
    </div>
</template>

<script>
import { AxiosInstance } from '../plugins/axios'

export default {
    data () {
        return {
            customuser: {
                username: '',
                password: '',
                password2: '',
                email: '',
                first_name: '',
                last_name_prefix: '',
                last_name: ''
            }
        }
    },
    methods: {
        register: function (e) {
            AxiosInstance.post('http://127.0.0.1:8000/account/register/',
                this.customuser
            )
            .then(response => {
                this.$router.push('/login')
            })
            .catch(err => {
                console.log(err)
            })
        }
    }
}
</script>
