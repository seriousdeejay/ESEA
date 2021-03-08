<template>
<div class="p-p-5" style="border-color: #00008B; border: 1px solid lightgrey; border-radius: 5px;">
            <p class="p-text-left">{{question.name}}</p>
            <Divider />
            <answer-input
            :value="answer || question.default"
            :type="question.answertype"
            :options="question.options"
            :readonly="readonly"
            option-value-key="text"
            required
            @input="changeAnswer"
            />
            <div v-if="question.description">
                <p class="p-text-justify p-text-light p-m-0" style="color: lightgrey;"><small>Description:</small><br>
                <small><small>{{question.description}}</small></small></p>
            </div>
            <div v-else>
                <p  class="p-text-left p-m-0"><small>No Description</small>
                </p></div>
</div>
</template>

<script>
    import AnswerInput from './AnswerInput'

export default {
    components: {
        AnswerInput
    },
    props: {
        question: {
            type: Object,
            required: true
        },
        answer: {
            type: String,
            default: undefined
        },
        readonly: {
            type: Boolean,
            default: false
        }
    },
    computed: {
        primaryBorder () {
            return { 'border-color': '#00008B' }
        }
    },
    methods: {
        changeAnswer (answer) {
            console.log(answer)
            this.$emit('input', answer)
        }
    }
}
</script>
