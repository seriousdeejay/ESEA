<template>
<div class="p-p-5" style="border-color: #00008B; border: 1px solid lightgrey; border-radius: 5px;">
            <p class="p-text-left"><span v-if="checkanswerrequired" style="color: red; font-size: 25px">*</span>{{question.name}}</p>
            <Divider />
            <answer-input
            :value="goodanswer || question.default"
            :type="question.answertype"
            :options="question.options"
            :readonly="readonly"
            :checkanswerrequired="checkanswerrequired"
            option-value-key="text"
            required
            @input="changeAnswer"
            />
            <div v-if="question.description">
                <p class="p-text-justify p-text-light p-m-0" style="color: lightgrey;"><small>Description:</small><br>
                <small><small>{{question.description}}</small></small></p>
            </div>
            <div v-else>
                <p  class="p-text-left p-m-0" style="color: lightgrey;"><small>No Description</small>
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
        },
        checkanswerrequired: {
            type: Boolean,
            default: false
        }
    },
    computed: {
        primaryBorder () {
            return { 'border-color': '#00008B' }
        },
        goodanswer () {
            if (this.question.answertype === ('RADIO' || 'CHECKBOX')) {
                return this.answer[0]
            }
            return this.answer[1]
        }
    },
    methods: {
        changeAnswer (answer) {
            this.$emit('input', { answer: answer, answertype: this.question.answertype })
        }
    }
}
</script>
