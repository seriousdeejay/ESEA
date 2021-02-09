<template>
    <h1>Hi</h1>
</template>

<script>
import { AxiosInstance } from '../plugins/axios'
import { mapState } from 'vuex'
// import { required, minLength } from 'vuelidate/lib/validators'

export default {
    data () {
        return {
            organisation: null
        }
    },
    methods: {
        // createpost: function (e) {
        //         AxiosInstance
        //             .post('http://127.0.0.1:8000/posts/',
        //                 this.post
        //             )
        //             .then(response => {
        //                 this.$router.push('/')
        //             })
        // }
    },
    computed: mapState(['accessToken', 'currentuser']),
    created () {
        AxiosInstance.get(`/networks/${this.$route.params.id}/`, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
          .then(response => { this.organisation = response.data })
          .catch(err => { console.log(err) })
    }

}
</script>
