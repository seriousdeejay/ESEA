<template>
    <div v-if="active">
        <form ref="form" class="p-fluid" @submit.prevent="!v$.$invalid">
            <div class="p-field p-mb-5">
                <span class="p-float-label">
                    <InputText id="topicname" ref="input" v-model="lazyTopic.name" :placeholder="nameLabel" :class="{'p-invalid': submitted && !lazyTopic.name }" @blur="updateName" />
                </span>
                <div class="p-error p-text-italic" v-for="error in nameErrors" :key="error"><small>{{error}}</small></div>
            </div>
            <div v-if="!lazyTopic.parent_topic" class="p-field">
                <span class="p-float-label">
                    <InputText v-model="lazyTopic.description" placeholder="Topic Description" @blur="updateDescription" />
                </span>
                <div class="p-error p-text-italic" v-for="error in descriptionErrors" :key="error"><small>{{error}}</small></div>
            </div>
        </form>
    </div>
    <topic-card v-else :name="lazyTopic.name" :description="lazyTopic.description" :is-sub-topic="!isMainTopic" />
</template>

<script>
import { isEqual } from 'lodash'
import HandleValidationErrors from '../../utils/HandleValidationErrors'
import { required, maxLength } from '../../utils/validators'
import useVuelidate from '@vuelidate/core'
import TopicCard from '../../components/cards/TopicCard'

export default {
    emits: [''],
    components: {
        TopicCard
    },
    props: {
        topic: {
            type: Object,
            required: true
        },
        active: {
            type: Boolean,
            default: false
        },
        errors: {
            type: Object,
            default: () => ({})
        }
    },
    data () {
        return {
            lazyTopic: { ...this.topic }
        }
    },
    computed: {
        isMainTopic () {
            return !this.lazyTopic.parent_topic
        },
        nameLabel () {
            return this.isMainTopic ? 'Topic name' : 'Sub topic name'
        },
        nameErrors () {
            return HandleValidationErrors(
                this.$v.lazyTopic.name,
                this.errors.name
            )
        },
        descriptionErrors () {
            return HandleValidationErrors(
                this.v$.lazyTopic.description,
                this.errors.description
            )
        }
    },
    watch: {
        topic (val) {
            if (!isEqual(this.lazyTopic, val)) {
                this.lazyTopic = { ...val }
            }
        },
        'v$.lazyTopic$invalid': function () {
            if (this.v$.lazyTopic.$invalid) { return }
            if (isEqual(this.topic, this.lazyTopic)) { return }
            this.$emit('input', this.lazyTopic)
        },
        active (val) {
            if (!val) {
                this.v$.$touch()
            } else {
                this.$nextTick(() => this.$refs.input && this.$refs.input.focus())
            }
        }
    },
    setup: () => ({ v$: useVuelidate() }),
    validations: {
        lazyTopic: {
            name: { required, maxLength: maxLength(120) },
            description: {}
        }
    },
    mounted () {
        if (!this.lazyTopic.name) {
            this.$refs.input.focus()
        }
    },
    created () {
        this.initialize()
    },
    methods: {
        initialize () {
            if (!this.lazyTopic.name) {
                const name = this.lazyTopic.parent_topic ? 'subtopic' : 'topic'
                this.lazyTopic.name = `Untitled ${name}`
            }
        },
        updateName () {
            this.v$.lazyTopic.name.$touch()
        },
        updateDescription () {
            this.v$.lazyTopic.description.$touch()
        }
    }
}
</script>
