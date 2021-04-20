<template>
    <form v-if="active" ref="form" class="p-fluid p-input-filled p-p-5" @submit.prevent="!v$.$invalid" :style="cssProps">
        <div class="p-field p-mb-3">
            <span class="p-float-label">
                <InputText id="topicname" ref="input" v-model="lazyTopic.name" :placeholder="nameLabel" :class="{'borderless': nameErrors.length }" @blur="updateName" />
            </span>
            <div class="p-error p-text-italic" v-for="error in nameErrors" :key="error"><small>{{error}}</small></div>
        </div>
        <div v-if="!lazyTopic.parent_topic" class="p-field">
            <span class="p-float-label">
                <InputText v-model="lazyTopic.description" placeholder="Topic Description" class="p-inputtext-sm" @blur="updateDescription" @focus="$event.target.select()" />
            </span>
            <div class="p-error p-text-italic" v-for="error in descriptionErrors" :key="error"><small>{{error}}</small></div>
        </div>
    </form>
    <topic-card v-else :name="lazyTopic.name" :description="lazyTopic.description" :is-sub-topic="!isMainTopic" style="border: 1px solid #e8e8e8;" />
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
                this.v$.lazyTopic.name,
                this.errors.name
            )
        },
        descriptionErrors () {
            return HandleValidationErrors(
                this.v$.lazyTopic.description,
                this.errors.description
            )
        },
        cssProps () {
            const props = { border: '1px solid lightgrey' }
            if (this.active) {
                props.border = '2px solid #9ecaed'
                props['background-color'] = 'white'
            }
            return props
        }
    },
    watch: {
        topic (val) {
            if (!isEqual(this.lazyTopic, val)) {
                this.lazyTopic = { ...val }
            }
        },
        lazyTopic: {
            handler (val) {
            setTimeout(() => {
                if (this.v$.lazyTopic.$invalid) { return }
                if (isEqual(this.topic, this.lazyTopic)) { return }
                this.$emit('input', this.lazyTopic)
                }, 200)
            },
            deep: true
        },
        active (val) {
            if (!val) {
                this.v$.$touch()
            } else {
                // this.$nextTick(() => this.$refs.input && this.$refs.input.focus())
            }
        }
    },
    setup: () => ({ v$: useVuelidate() }),
    validations: {
        lazyTopic: {
            name: { required, maxLength: maxLength(120), $lazy: true },
            description: { maxLength: maxLength(255), $lazy: true }
        }
    },
    mounted () {
        if (!this.lazyTopic.name) {
            this.$refs.topicname.focus()
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

<style lang="scss" scoped>
.p-inputtext {
    border: none;
    border-bottom: 1px solid lightgrey;
}
.borderless {
    border-bottom: 1px solid red;

}
</style>
