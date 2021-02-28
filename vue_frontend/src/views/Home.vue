<template>
<h3>Advanced</h3>
<FileUpload name="myfile" url="http://localhost:8000/import-yaml/" @upload="onUpload" :multiple="true" accept="" :maxFileSize="1000000">
    <template #empty>
        <p>Drag and drop files to here to upload.</p>
    </template>
</FileUpload>
<h1>Test</h1>
<!-- <div v-for="organisation in org" :key="organisation.id">{{ organisation.name }} - 1</div>
{{ organisations.name }} -->
<div v-for="organisation in organisations" :key="organisation.name">{{organisation.name}}</div>
</template>

<script>
// import { AxiosInstance } from '../plugins/axios'
import { mapState, mapActions } from 'vuex'

export default {
    data () {
        return {
            org: [],
            post: {
                title: '',
                content: ''
            },
            submitted: false
        }
    },
    computed: {
    ...mapState('organisation', ['organisations'])
    },
    created () {
        this.initialize()
    },
    methods: {
        ...mapActions('network', ['fetchNetworks']),
        ...mapActions('organisation', ['fetchOrganisations']),
        ...mapActions('user', ['fetchUsers']),
        async initialize () {
            await this.fetchNetworks({})
            await this.fetchOrganisations({})
            await this.fetchUsers({})
       }
    }
}
        // AxiosInstance.get(`http://127.0.0.1:8000/organisations/${this.$route.params.id}/`)
        //     .then(response => {
        //         console.log(response.data)
        //         this.post = response.data
        //     })

    // <div class="companydetails">
    //      <form @submit.prevent="updatecompany" method="post">
    //         <div class="">
    //             <label for="title">Title</label>
    //             <input
    //                 type="text"
    //                 id="title"
    //                 v-model="post.title"
    //                 name="title"
    //                 placeholder="enter title"
    //             >
    //         </div>
    //         <div class="">
    //             <label for="content">Content</label>
    //              <input
    //                 type="text"
    //                 id="content"
    //                 v-model="post.content"
    //                 name="content"
    //                 placeholder="enter content"
    //             >
    //         </div>
    //         <button type="submit" class="btn btn-primary">Submit</button>
    //     </form>
    // </div>
</script>
