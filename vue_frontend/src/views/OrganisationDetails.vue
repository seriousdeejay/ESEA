<template>
<h1> Test</h1>

<h1>{{organisation.id }} {{ organisation.name }} {{ organisation.participants }}</h1>
{{ organisationusers }}
<br>
<br>
<div v-for="user in organisationusers" :key="user.id">
    {{ user.username }}
</div>
    <!--
    <div class="organisations">
        <div v-if="organisation">
            <DataTable ref="dt" :value="organisation">
                <Column field="ispublic" header="Public" :sortable="true"></Column>
                <Column field="name" header="Name" :sortable="true"></Column>
                <Column field="description" header="Description" :sortable="true"></Column>
            </DataTable>
        </div>
        <div v-else>Organisations are being loaded...</div>
    </div>
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

            <div class="p-field p-grid">
                <label for="title" class="p-col" >owner</label>
                 <div class="p-col">
                    <InputText type="text" id="owner" v-model="post.owner" />
                </div>
            </div>
                {{currentuser}}
            <div style="text-align:right">
                <Button type="submit" value="submit">Create Post</Button>
            </div>
        </form>
    </div> -->
</template>

<script>
import { AxiosInstance } from '../plugins/axios'
import { mapState } from 'vuex'
// import { required, minLength } from 'vuelidate/lib/validators'

export default {
    data () {
        return {
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
    computed: mapState(['accessToken', 'currentuser', 'organisation', 'organisationusers']),
    created () {
        AxiosInstance.get(`/organisations/${this.$route.params.id}/`, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
          .then(response => { this.$store.state.organisation = response.data })
          .catch(err => { console.log(err) })
        AxiosInstance.get(`/organisationparticipants/${this.$route.params.id}/`, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
        .then(response => { this.$store.state.organisationusers = response.data })
        .catch(err => { console.log(err) })
    }

}
</script>
