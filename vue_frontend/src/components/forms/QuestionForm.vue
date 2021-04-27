<template>
        <form ref="form" class="p-grid p-px-5 p-pt-5 p-fluid p-input-filled" :style="cssProps" >
            <div class="p-grid p-col-12 p-mx-0 p-px-0 p-field">
                 <div class="p-col-4">
                    <span class="p-float-label">
                        <InputText id="questionkey" type="text" v-model="lazyQuestion.key"  :class="{'borderless': keyErrors.length}"  @blur="questionKeyFilter" :disabled="!active" />
                        <label for="questionkey">Question Key</label>
                    </span>
                    <div class="p-error p-text-italic" v-for="error in keyErrors" :key="error"><small>{{error}}</small></div>
                </div>
                <div class="p-col-4">
                    <Dropdown v-model="lazyQuestion.answertype" :options="questionTypesList" optionLabel="text" optionValue="value" placeholder="Select a Type" @change="changeQuestionType" :disabled="!active" />
                </div>
                <div class="p-col-4">
                    <ToggleButton v-model="lazyQuestion.isMandatory" onLabel="Mandatory" offLabel="not Required" onIcon="pi pi-check" offIcon="pi pi-times" :disabled="!active" />
                </div>
            </div>
                <div class="p-col-12 p-field">
                    <span class="p-float-label">
                        <InputText id="questionname" type="text" v-model="lazyQuestion.name"  :class="{'borderless': nameErrors.length}"  @blur="v$.lazyQuestion.name.$touch()" :disabled="!active" />
                        <label for="questionname">Question</label>
                    </span>
                    <div class="p-error p-text-italic" v-for="error in nameErrors" :key="error"><small>{{error}}</small></div>
                </div>
            <template v-if="active">
            <div class="p-col-12 p-field">
                <span class="p-float-label">
                    <InputText id="questiondescription" type="text" v-model="lazyQuestion.description" :disabled="!active" />
                    <label for="questiondescription">Description</label>
                </span>
            </div>
                <div v-if="active && lazyQuestion.answertype === 'NUMBER'" class="p-grid p-col-12 p-mx-0 p-px-0">
                    <div class="p-col-4">
                        <span class="p-float-label">
                            <InputText id="minvalue" type="number" v-model="lazyQuestion.min_number" />
                            <label for="minvalue">Minimum</label>
                        </span>
                    </div>
                    <div class="p-col-4">
                        <span class="p-float-label">
                            <InputText id="defaultvalue" type="number" v-model="lazyQuestion.default" />
                            <label for="defaultvalue">Default</label>
                        </span>
                    </div>
                    <div class="p-col-4">
                        <span class="p-float-label">
                            <InputText id="maxvalue" type="number" v-model="lazyQuestion.max_number" />
                            <label for="maxvalue"><small>Maximum</small></label>
                        </span>
                    </div>
                </div>
                <div v-if="active && lazyQuestion.options && lazyQuestion.options.length" class="p-grid p-col-12 p-mx-0 p-px-0">
                    <option-form v-for="(option, index) in lazyQuestion.options" :key="`option-${index}`" :option="option" @delete="deleteOption(option)" />
                    <Button label="Add Option" class="p-button-text" @click="newOption" />
                </div>
            </template>
        </form>
        <!-- <div v-else class="p-grid p-jc-center p-ai-center p-px-5" :style="cssProps">
            <i class="pi pi-question p-col-1" style="fontSize: 2rem"></i>
            <div class="p-col-11">
            <p><span class="p-text-bold">Question:</span> {{ question.name }}</p>
            <div class="p-d-flex p-jc-between p-mr-5 p-pr-5">
            <p><span class="p-text-bold">Key:</span> {{ question.key }}</p>
            <p><span class="p-text-bold">Type:</span> {{ questionType }}</p>
            </div>
            </div>
            <Divider />
            <div v-if="!question.options.length" class="p-d-flex p-jc-between p-col-10">
                <p v-if="question.min_number"><span class="p-text-bold">Minimum:</span> {{ question.min_number }}</p>
                <p><span class="p-text-bold">Default:</span> {{ question.default }}</p>
                <p v-if="question.max_number"><span class="p-text-bold">Maximum:</span> {{ question.max_number }}</p>
            </div>
            <template v-else>
                <div v-for="(option, index) in question.options" :key="index" class="p-field-checkbox p-col-12">
                    <Checkbox :id="index" name="option" :value="text" v-model="ss" />
                    <label :for="index"><span class="p-text-bold">Text:</span> '{{option.text}}'<span class="p-text-bold"> - Value:</span> '{{option.value}}'</label>
                </div>
            </template>
        </div> -->
</template>
<script>
import { mapGetters } from 'vuex'
import useVuelidate from '@vuelidate/core'
import { QUESTION_TYPES } from '../../utils/constants'
import HandleValidationErrors from '../../utils/HandleValidationErrors'
import { isEqual, cloneDeep } from 'lodash'
import { required, maxLength } from '../../utils/validators'
import Dropdown from 'primevue/dropdown'
import OptionForm from '../../components/forms/OptionForm'

export default {
    components: {
        OptionForm,
        Dropdown
    },
    props: {
        question: {
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
            lazyQuestion: cloneDeep(this.question) || { },
            questionTypes: QUESTION_TYPES
        }
    },
    computed: {
        ...mapGetters('question', ['getValidQuestionKeyNumber']),
        questionTypesList () {
            return Object.entries(this.questionTypes).map(([text, value]) => ({ text, value }))
        },
        questionType () {
            return this.questionTypesList.find(type => type.value === this.lazyQuestion.answertype).text
        },
        keyErrors () {
            return HandleValidationErrors(this.v$.lazyQuestion.key, this.errors.key)
        },
        nameErrors () {
            return HandleValidationErrors(this.v$.lazyQuestion.name, this.errors.name)
        },
        cssProps () {
            const props = { border: '1px solid lightgrey' }
            if (this.active) {
                props.border = '2px solid #9ecaed'
                props['background-color'] = '#f7f7f7'
            }
            return props
        }
    },
    watch: {
        question (val) {
            if (isEqual(this.lazyQuestion, val)) { return }
            this.lazyQuestion = cloneDeep(val)
        },
        lazyQuestion: {
            handler (val) {
                setTimeout(() => {
                if (this.v$.lazyQuestion.$invalid) { return }
                if (isEqual(this.question, val)) { return }
                this.$emit('input', cloneDeep(val))
                }, 200)
            },
            deep: true
        },
        active (val) {
            if (!val) {
                this.v$.$touch()
            } else {
                this.$nextTick(() => this.$refs.input && this.$refs.input.focus())
            }
        }
    },
    mounted () {
        if (!this.lazyQuestion.name) {
            this.$refs.input.focus()
        }
    },
    created () {
        this.initialize()
    },
    setup: () => ({ v$: useVuelidate() }),
    validations: {
        lazyQuestion: {
            key: { required },
            name: { required, maxLength: maxLength(120) }
        }
    },
    methods: {
        initialize () {
            if (!this.lazyQuestion.key && !this.lazyQuestion.name) {
                this.lazyQuestion.key = `direct_indicator_${this.getValidQuestionKeyNumber}`
                this.lazyQuestion.name = `question_${this.getValidQuestionKeyNumber}`
            }
            if (!this.lazyQuestion.options) {
                this.lazyQuestion.options = []
            }
        },
        updateName () {
            this.v$.lazyQuestion.name.$touch()
        },
        changeQuestionType (e) {
            this.lazyQuestion.answertype = e.value
            const typesWithOptions = ['RADIO', 'CHECKBOX']
            if (typesWithOptions.includes(e.value) && !this.lazyQuestion.options.length) {
                this.lazyQuestion.options = [
                    { text: 'option 1', value: 1 },
                    { text: 'option 2', value: 2 }
                ]
            } else if (!typesWithOptions.includes(e)) {
                this.lazyQuestion.options = []
            }
        },
        newOption () {
            this.lazyQuestion.options.push({ text: `option ${this.lazyQuestion.options.length + 1}`, value: '' })
        },
        deleteOption (event) {
            if (this.lazyQuestion.options && this.lazyQuestion.options.length > 2) {
                this.lazyQuestion.options = this.lazyQuestion.options.filter(option => option !== event)
            }
        },
        questionKeyFilter (val) {
            if (val.includes(' ')) {
                this.lazyQuestion.key = val.replace(' ', '_')
            }
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
