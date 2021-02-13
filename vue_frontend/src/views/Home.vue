<template>
<h1>Test</h1>
<div v-for="organisation in org" :key="organisation.id">{{ organisation.name }} - 1</div>
{{ organisations }}
<div v-for="organisation in organisations" :key="organisation.name">{{organisation.name}}</div>
</template>

<script>
// import { AxiosInstance } from '../plugins/axios'
import { mapState, mapActions } from 'vuex'
import TestService from '../services/TestService'

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
        this.initialize2()
        this.initialize()
    },
    methods: {
        ...mapActions('organisation', ['fetchOrganisations']),
        async initialize () {
            await TestService.get()
            .then(response => {
                this.org = response.data
            })
            .catch(err => {
            console.log(err)
          })
//             // await this.fetchOrganisations({})
       },
       async initialize2 () {
           console.log('check')
           await this.fetchOrganisations({})
           console.log('check2')
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
