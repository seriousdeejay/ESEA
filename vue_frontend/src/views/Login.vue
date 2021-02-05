<template>

<Card style="width: 25rem; margin-bottom: 2em" class="p-d-block p-mx-auto">
    <template #title>
        Login
    </template>
    <template #content>
        <p v-if="incorrectAuth">Incorrect username or password entered - please try again!</p>
        <form v-on:submit.prevent="login">
        <div class="p-field p-grid">
            <label for="username" class="p-col-fixed" style="width:100px">Username</label>
            <div class="p-col">
                <InputText type="text" id="username" v-model="username" />
            </div>
        </div>
        <div class="p-field p-grid">
            <label for="password" class="p-col-fixed" style="width:100px">Password</label>
            <div class="p-col">
                <Password id="password" v-model="password" :feedback="false" />
            </div>
        </div>
        <Button type="submit" label="Submit" value="submit">Login</Button>
        </form>
    </template>
</Card>
</template>

<script>
export default {
    name: 'login',
    data () {
        return {
            username: '',
            password: '',
            incorrectAuth: false
        }
    },
    methods: {
        login () {
            this.$store.dispatch('userLogin', {
                username: this.username,
                password: this.password
            })
            .then(() => {
                this.$router.push({ name: 'posts' })
            })
            .catch(err => {
                console.log(err)
                this.incorrectAuth = true
            })
        }
    }
}
</script>
