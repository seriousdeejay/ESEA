<template>

<Menubar :model="items" v-if="accessToken!=null">
     <template #start>
        <img alt="logo" src="./assets/logo.png" height="40" class="p-mr-5">
    </template>
    <template #end>
      <Button type="button" :label="'account ('+ currentuser + ')'" @click="toggle" aria-haspopup="true" aria-controls="profile_menu" class="p-button-raised p-button-text p-button-plain"/>
      <Menu id="profile_menu" ref="menu" :model="profile" :popup="true"/>
      <!--<Button label="Logout" icon="pi pi-power-off" :style="{'margin-left': '0 .5em'}"/>-->
    </template>
</Menubar>
  <div id="nav">
    <!-- <router-link to="/">Dashboard</router-link> |
    <router-link to="/home">Home</router-link> |
    <router-link to="/about">About</router-link> -->
  </div>
  <router-view/>
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
          to: '/home',
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
          items: [
            {
              label: 'Left',
              icon: 'pi pi-fw pi-align-left'
            }
          ]
        },
        {
          label: 'organisations',
          icon: 'pi pi-globe',
          items: [
            {
              label: 'Left',
              icon: 'pi pi-fw pi-align-left'
            }
          ]
        },
        {
          label: 'Methods',
          icon: 'pi pi-briefcase',
          to: '/'
        },
         {
          label: 'Users',
          icon: 'pi pi-users',
          to: 'users'
        }
      ],
      profile: [
            {
              label: 'Personal Details',
              icon: 'pi pi-id-card',
              to: 'userprofile'
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
  computed:
    mapState(['accessToken', 'currentuser'])
}
</script>

<style lang="scss">
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
</style>
