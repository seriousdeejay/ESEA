<template>
  <div v-if="accessToken!=null"> <!--style="min-height: 800px; height: auto; min-width: 1100px; background-color: #F8F9FA;"-->
    <Menubar :model="items" v-if="accessToken!=null" class="p-shadow-5" style="background-color: #EFEEEE; position: fixed; width: 100%; z-index: 1000;">
        <template #start>
            <img alt="logo" src="./assets/logo.png" height="40" class="p-mr-5">
        </template>
        <template #end>
          <Button type="button" :label="'account ('+ currentuser + ')'" @click="toggle" aria-haspopup="true" aria-controls="profile_menu" class="p-button-raised p-button-text p-button-plain"/>
          <Menu id="profile_menu" ref="menu" :model="profile" :popup="true" />
        </template>
    </Menubar>
    <my-bread-crumb />
    <!-- <h1>Breadcrumb with Chosen Network>Chosen Organisation>Chosen Method</h1> -->
    <router-view />
  </div>
  <div v-else class="centered">
    <router-view style="background-color: white;" />
  </div>
    <router-view class="anonymous view" name="anonymousview"/>
</template>
<script>
import { mapState } from 'vuex'
import MyBreadCrumb from './components/MyBreadCrumb'

export default {
  components: {
    MyBreadCrumb
  },
  data () {
    return {
      items: [
        {
          label: 'Home',
          // icon: 'pi pi-home',
          to: '/',
          items: [
            {
              label: 'New',
              icon: 'pi pi-fw pi-plus'
            },
            {
              separator: true
            },
            {
              label: 'Export',
              icon: 'pi pi-fw pi-external-link'
            }
          ]
        },
        {
          label: 'Networks',
          icon: 'pi pi-cloud',
          to: '/networks',
          items: [
            {
              label: 'Information',
              icon: 'pi pi-fw pi-align-left'
            }
          ]
        },
        {
          label: 'Organisations',
          icon: 'pi pi-globe',
          to: '/organisations',
          items: [
            {
              label: 'Information',
              icon: 'pi pi-fw pi-align-left'
            }
          ]
        },
        {
          label: 'Methods',
          icon: 'pi pi-briefcase',
          to: '/methods'
        },
        {
          label: 'Users',
          icon: 'pi pi-users',
          to: '/users'
        }
      ],
      profile: [
            {
              label: 'Personal Details',
              icon: 'pi pi-id-card',
              to: '/userprofile'
            },
            {
              label: 'Log out',
              icon: 'pi pi-sign-out',
              to: '/logout'
            }
      ]
    }
  },
  methods: {
   toggle (event) {
            this.$refs.menu.toggle(event)
        }
  },
  computed: {
    ...mapState('authentication', ['accessToken', 'currentuser'])
    // isIdle () {
    //   return this.$store.state.idleVue.isIdle
    // },
    // onIdle () {
    //   console.log('user idled')
    //   return this.$store.state.idleVue
    // }
  }
}
</script>

<style lang="scss">
body, html, #app {
  min-height: 100%;
  background-color: #F8F9FA;
  margin: 0 0;
  }

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}

.centered {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>
