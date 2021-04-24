<template>
    <div class="p-px-5 p-py-1 p-shadow-2" style="border-bottom: 2px solid lightgrey; background-color: #f1f1f1;"> <!-- #dcdcdc"> -->
        <h3 v-if="isSubTopic">
            Subtopic: <span class="p-text-light p-text-italic">{{ name }}</span>
        </h3>
        <h2 v-else>
            Parenttopic: <span class="p-text-light p-text-italic">{{ name }}</span>
        </h2>
        <p v-if="description">
            {{ description }}
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
