<template>

<div style="width: 30rem; border-radius:0.25rem" class="p-d-block p-mx-auto p-p-5 p-shadow-10">
            <h1>Create An Account</h1>
        <p v-if="incorrectAuth">Incorrect username or password entered - please try again!</p>
        <form v-on:submit.prevent="">
            <div class="p-field p-grid">
                <label for="username" class="p-col">Username</label>
                <div class="p-col">
                    <InputText type="text" id="username" v-model="username" />
                </div>
            </div>
            <div class="p-field p-grid">
                <label for="password" class="p-col" >Password</label>
                <div class="p-col">
                    <Password id="password" v-model="password" :feedback="false" />
                </div>
            </div>

            <div style="text-align:right">
                <Button type="submit" value="submit">Login</Button>
            </div>
        </form>
        <br>
        <hr>
        <div class="p-d-flex p-jc-between p-ai-center">
            <h4>No Account yet?</h4>
            <div>
            <Button @click="$router.push('home')" class="p-button-secondary" disabled="disabled">Create Account</Button>
        </div>
        </div>
        <div class="p-text-left">
            <small>Add assessments, get peer reviews, share and find out what your organisations
                needs now and in the future!</small>
        </div>
</div>
</template>
