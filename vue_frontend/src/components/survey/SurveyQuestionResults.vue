<template>
    
</template>

<script>
import { QUESTION_TYPES } from '@/utils/Constants'
export default {
    components: {
    },
    props: {
        question: {
            type: Object,
            required: true,
        },
        answers: {
            type: Array,
            default: () => []
        }
    },
    data () {
        return {
            questionTypes: QUESTION_TYPES
        }
    },
    computed: {
        type () {
            return this.question.answertype
        },
        average () {
            if (!this.answers.length || this.type !== this.questionTypes.NUMBER) {
                return 0;
            }
		}
    }
}
</script>