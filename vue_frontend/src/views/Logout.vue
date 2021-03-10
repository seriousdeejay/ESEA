<template>
  <div class="log">
    Log out
  </div>
</template>

<script>
import { mapActions } from 'vuex'
  export default {
    created () {
      this.userLogout()
      this.$router.push({ name: 'login' })
    },
    methods: {
      ...mapActions('authentication', ['userLogout'])
    }
  }
</script>
