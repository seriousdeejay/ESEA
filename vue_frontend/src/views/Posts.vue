<template>
    <div style="margin: 0px 50px">
        <div class="p-grid">
            <div v-for="posts in APIData" :key="posts.id"  class="p-col-4">
                <Card style="margin-bottom: 2em" class="p-shadow-5">
                    <template #title>
                        {{ posts.title }}
                    </template>
                    <template #content>
                        <p> {{ posts.content }}</p>
                        <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
                    </template>
                    <template #footer>
                        <div class="p-d-flex">
                        <Button icon="pi pi-chevron-down" label="View" />
                        <Button icon="pi pi-pencil" label="Edit" class="p-button-secondary" style="margin-left: .5em" />
                        <p class="p-ml-auto">9 min</p>
                        </div>
                    </template>
                </Card>
            </div>
        </div>
    </div>
</template>

<script>
import { AxiosInstance } from '../plugins/axios'

export default {
    name: 'Posts',
    data () {
        return {
            APIData: []
        }
    },
    components: {
    },
    created () {
        AxiosInstance.get('/posts/')
            .then(response => {
                console.log('Post API has received data')
                this.APIData = response.data
            })
            .catch(err => {
                console.log(err)
            })
    }
}
</script>
