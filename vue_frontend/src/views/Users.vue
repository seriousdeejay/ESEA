<template>
    <div class="users">
        <h1>Users</h1>
    </div>
</template>

<script>
export default {
mounted () {
    this.$toast.add({ severity: 'success', summary: 'Success Message', detail: 'Order submitted', life: 3000 })
    }
}
</script>
