<template>
    <div class="userprofile">
        <h1 class="title">
            User Profile - {{ currentuser }}
        </h1>
    </div>
</template>

<script>
import store from '../store'

export default {
    computed: {
        currentuser () {
            return store.state.currentuser
        }
    }
}
</script>
