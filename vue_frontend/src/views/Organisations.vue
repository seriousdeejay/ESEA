<template>
    <div class="organisations">
        <h1>Organisations</h1>
        <form @submit.prevent="createpost" method="post">
            <div class="p-field p-grid">
                <label for="title" class="p-col">title</label>
                <div class="p-col">
                    <InputText type="text" id="title" v-model="post.title" />
                </div>
            </div>
            <div class="p-field p-grid">
                <label for="title" class="p-col" >Content</label>
                 <div class="p-col">
                    <InputText type="text" id="content" v-model="post.content" />
                </div>
            </div>

            <!-- <div class="p-field p-grid">
                <label for="title" class="p-col" >owner</label>
                 <div class="p-col">
                    <InputText type="text" id="owner" v-model="post.owner" />
                </div>
            </div> -->
                {{currentuser}}
            <div style="text-align:right">
                <Button type="submit" value="submit">Create Post</Button>
            </div>
        </form>
    </div>
</template>

<script>
import { AxiosInstance } from '../plugins/axios'
import { mapState } from 'vuex'
// import { required, minLength } from 'vuelidate/lib/validators'

export default {
    data () {
        return {
            post: {
                title: '',
                content: '',
                owner: this.currentuser
            }
        }
    },
    methods: {
        createpost: function (e) {
                AxiosInstance
                    .post('http://127.0.0.1:8000/posts/',
                        this.post
                    )
                    .then(response => {
                        this.$router.push('/')
                    })
        }
    },
    computed: mapState(['accessToken', 'currentuser'])

}

</script>
