<template>
    <div class="companydetails">
         <form @submit.prevent="updatecompany" method="post">
            <div class="">
                <label for="title">Title</label>
                <input
                    type="text"
                    id="title"
                    v-model="post.title"
                    name="title"
                    placeholder="enter title"
                >
            </div>
            <div class="">
                <label for="content">Content</label>
                 <input
                    type="text"
                    id="content"
                    v-model="post.content"
                    name="content"
                    placeholder="enter content"
                >
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</template>

<script>
import { AxiosInstance } from '../plugins/axios'
export default {
    data () {
        return {
            post: {
                title: '',
                content: ''
            },
            submitted: false
        }
    },
    mounted () {
        AxiosInstance.get(`http://127.0.0.1:8000/posts/${this.$route.params.id}/`)
            .then(response => {
                console.log(response.data)
                this.post = response.data
            })
    }
}
</script>
