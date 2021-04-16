<template>
    <p :class="isSubTopic ? '' : 'p-text-bold'">
        {{ name }}
    </p>
    <p v-if="description">
        {{ description }}
    </p>
</template>

<script>
export default {
    props: {
        name: {
            type: String,
            required: true
        },
        description: {
            type: String,
            default: undefined
        },
        isSubTopic: {
            type: Boolean,
            default: false
        }
    }
}
</script>
