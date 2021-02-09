<template>
    <div>
        <h1>
        to do:
        -List of Methods (just like Network and Organisations)
        </h1>
    </div>
    <div style="margin: 0px 50px">
         <h1>-Posts-</h1>
        <div class="p-grid">
            <div v-for="organisation in APIData" :key="organisation.id"  class="p-col-4">
                <!-- <div v-if="organisation.ispublic"> -->
                <Card style="margin-bottom: 2em" class="p-shadow-5">
                    <template #title>
                        {{ organisation.name }}
                    </template>
                    <template #content>
                        <p> {{ organisation.description }}</p>
                        <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
                    </template>
                    <template #footer>
                        <div class="p-d-flex">
                        <Button icon="pi pi-chevron-down" label="View" />
                        <Button icon="pi pi-pencil" label="Edit" @click="$router.push({name: 'editorganisation', params: { id: organisation.id }})" class="p-button-secondary" style="margin-left: .5em" />
                         <p class="p-ml-auto">{{ organisation.creator }} 9 min</p>
                        </div>
                    </template>
                </Card>
                <!-- </div>
                <div v-else>Private Post</div> -->
            </div>
        </div>
    </div>
</template>

<script>
import { AxiosInstance } from '../plugins/axios'
import { mapState } from 'vuex'

export default {
    name: 'Organisations',
    onIdle () {
      this.$store.dispatch('userLogout')
        .then(() => {
          this.$router.push({ name: 'login' })
        })
    },
    data () {
        return {
        }
    },
    components: {
    },
    computed: mapState(['APIData']),
    created () {
        AxiosInstance.get('/personalorganisations/', { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
          .then(response => {
            this.$store.state.APIData = response.data
          })
          .catch(err => {
            console.log(err)
          })
    }
}
//         ('/posts/')
//             .then(response => {
//                 console.log('Post API has received data')
//                 this.APIData = response.data
//             })
//             .catch(err => {
//                 console.log(err)
//             })
//     }
// }
</script>
