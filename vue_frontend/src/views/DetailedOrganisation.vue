<template>
    <div class="organisations">
        <h1>Organisations</h1>
        <div v-if="organisations.length">
            <DataTable :value="organisations">
                <Column v-for="col of columns" :field="col.field" :header="col.header" :key="col.field"></Column>
            </DataTable>
        </div>
        <div v-else>Organisations are being loaded...</div>

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
            organisations: [],
            columns: null,
            post: {
                title: '',
                content: '',
                creator: this.currentuser
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
    computed: mapState(['accessToken', 'currentuser']),
    created () {
            this.columns = [
            { field: 'name', header: 'Name' },
            { field: 'description', header: 'Description' },
            { field: 'participants.length', header: 'Participants' },
            { field: 'title', header: 'Title' },
            { field: 'content', header: 'Content' }
        ]
        AxiosInstance.get('/organisations/', { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
          .then(response => { this.organisations = response.data })
          .catch(err => { console.log(err) })
    }
}
</script>
