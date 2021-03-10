<template>
  <div v-if="accessToken!=null" class="window card p-m-5 p-shadow-3" style="min-height: 800px; height: auto; min-width: 1100px; background-color: #F8F9FA;">
    <Menubar :model="items" v-if="accessToken!=null" style="background-color: #EFEEEE;">
        <template #start>
            <img alt="logo" src="./assets/logo.png" height="40" class="p-mr-5">
        </template>
        <template #end>
          <Button type="button" :label="'account ('+ currentuser + ')'" @click="toggle" aria-haspopup="true" aria-controls="profile_menu" class="p-button-raised p-button-text p-button-plain"/>
          <Menu id="profile_menu" ref="menu" :model="profile" :popup="true" />
        </template>
    </Menubar>
    <!-- <h1>Breadcrumb with Chosen Network>Chosen Organisation>Chosen Method</h1> -->
      <router-view/>
  </div>
  <div v-else class="centered">
    <router-view style="background-color: white;"/>
  </div>
</template>
<script>
import { mapState } from 'vuex'

export default {
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
          label: 'organisations',
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
        },
        {
          label: 'Log out',
          to: '/logout'
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
  }
}
</script>

<style lang="scss">
body, html, #app {
  min-height: 100%;
  background-color: lightgray;
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
