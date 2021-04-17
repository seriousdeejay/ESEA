<template>
    <div class="p-text-italic">
    <h3 :class="isSubTopic ? 'p-text-light' : ''">
        {{ name }}
    </h3>
    <p>
        {{ description || 'No Description' }}
    </p>
    </div>
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
