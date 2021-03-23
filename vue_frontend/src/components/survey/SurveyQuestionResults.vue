<template>
    <div class="p-p-5" style="border-color: #00008B; border: 1px solid lightgrey; border-radius: 5px;">
        <p class="p-text-left">{{ question.name }}</p>
        <Divider class="p-mb-4" />
    <div class="p-p-3 p-pt-5 p-my-3" style="border: 1px solid lightgrey;">
    <div v-if="answertype === questionTypes.RADIO || questionTypes.CHECKBOX">
        <div v-for="(mappedAnswer, index) in optionMappedAnswers" :key="index" class="p-grid p-d-flex p-ai-center p-m-1">
            <div class="p-col-fixed" style="width:80px">
                <div v-if="amountdisplaychoice.value">
                        {{ Math.round(mappedAnswer[1] / answers.length * 100 ) }}%
                </div>
                <div v-else>
                    {{ mappedAnswer[1] }}
                </div>
            </div>
            <div class="p-col p-text-left p-field-radiobutton p-m-0 p-p-0">
                <RadioButton  v-if="answertype === questionTypes.RADIO" :id="`${index}-option`" name="option" :value="mappedAnswer[0]" :disabled="true" />
                <Checkbox v-if="answertype === questionTypes.CHECKBOX" :id="`${index}-option`" name="option" :value="mappedAnswer[0]" :disabled="true" />
                <label :for="`${index}-option`" class="p-text-left">{{mappedAnswer[0]}}</label>
            </div>
        </div>
    </div>
    <div v-else>
        <div v-for="(answer, index) in answers" :key="index">
            {{answer}}
        </div>
        <p>average: {{ average }}</p>
    </div>
    </div>
        <div v-if="question.description">
                    <p class="p-text-justify p-text-light p-m-0" style="color: lightgrey;"><small>Description:</small><br>
                    <small><small>{{question.description}}</small></small></p>
        </div>
        <div v-else>
            <p  class="p-text-left p-m-0" style="color: lightgrey;"><small>No Description</small></p>
        </div>
        <div class="p-d-flex p-jc-center">
        <Chart v-if="answertype === questionTypes.RADIO" type="pie" :data="chartData" class="p-col" />
    </div>
        <!-- <Chart v-if="answertype === questionTypes.CHECKBOX" type="bar" :data="chartData" /> -->
    </div>
</template>

<script>
import { QUESTION_TYPES } from '../../utils/constants'
import Chart from 'primevue/chart'
export default {
    components: {
        Chart
    },
    props: {
        question: {
            type: Object,
            required: true
        },
        answers: {
            type: Array,
            default: () => []
        },
        amountdisplaychoice: {
            type: Boolean,
            default: false
        }
    },
    data () {
        return {
            questionTypes: QUESTION_TYPES,
            chartData: {
				labels: [],
				datasets: [
					{
                        label: 'Visualisation',
						data: [],
						backgroundColor: [
                            '#42A5F5',
                            '#66BB6A',
                            '#FFA726',
                            '#26C6DA',
                            '#7E57C2',
                            '#7AC142',
                            '#007CC3',
                            '#00529B',
                            '#377B2B'
                        ],
                        hoverBackgroundColor: [
                            '#64B5F6',
                            '#81C784',
                            '#FFB74D'
                        ]
					}
				]
			}
        }
    },
    computed: {
        answertype () {
            return this.question.answertype
        },
        average () {
            if (!this.answers.length || this.type !== this.questionTypes.NUMBER) {
                return 0
            }
            const total = this.answers.reduce(
                (a, b) => parseInt(a, 10) + parseInt(b, 10), 0)

            return total / this.answers.length
		},
        optionMappedAnswers () {
            const optionMappedAnswers = {}
            if (!this.question.options.length || !this.answers.length) {
				return optionMappedAnswers
            }

            this.question.options.forEach(
				option => (optionMappedAnswers[option.text] = 0)
			)
			let allAnswers = []
			if (this.answertype === this.questionTypes.CHECKBOX) {
				this.answers.forEach((answer) => {
					const list = answer.split(',')
					allAnswers = [...allAnswers, ...list]
				})
			} else if (this.answertype === this.questionTypes.RADIO) {
				allAnswers = this.answers
			}
			allAnswers.forEach(answer => (optionMappedAnswers[answer] += 1))
			return Object.entries(optionMappedAnswers)
		}
    },
    created () {
        this.initialize()
    },
    methods: {
        initialize () {
            this.optionMappedAnswers.forEach((answer) => {
                if (answer[1] > 0) {
                var val = Math.round(answer[1] / this.answers.length * 100)
                console.log(val)
                if (answer[0].length > 100) {
                    var label = 'A'
                    this.chartData.labels.push(label)
                } else {
                    this.chartData.labels.push(answer[0])
                }
                this.chartData.datasets[0].data.push(val)
                }
            })
        },
        changeAnswer (answer) {
            this.$emit('input', answer)
        }
    }
}
</script>

<style scoped>
.p-chart {
    width: 500px;
}
</style>
