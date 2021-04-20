<template>
        <form ref="form" v-if="active" class="p-grid p-px-5 p-pt-5" @submit.prevent="save" :style="cssProps"  >
            <div class="p-grid p-col-12 p-fluid">
                <div class="p-col-3 p-field">
                    <span class="p-float-label">
                        <InputText id="questionkey" type="text" v-model="lazyQuestion.key"  :class="{'borderless': true}"  @blur="questionKeyFilter"  />
                        <label for="questionkey">Question Key</label>
                    </span>
                    <!-- <div class="p-error p-text-italic" v-for="error in nameErrors" :key="error"><small>{{error}}</small></div> -->
                </div>
                <div class="p-col p-field">
                    <span class="p-float-label">
                        <InputText id="questionname" type="text" v-model="lazyQuestion.name"  :class="{'borderless': true}"  @blur="updateName"  />
                        <label for="questionname">Question</label>
                    </span>
                    <!-- <div class="p-error p-text-italic" v-for="error in nameErrors" :key="error"><small>{{error}}</small></div> -->
                </div>
            </div>
            <div class="p-grid p-col-12 p-fluid">
                <div class="p-col-3 p-field">
                    <Dropdown v-model="lazyQuestion.type" :options="questionTypesList" optionLabel="text" optionValue="value" placeholder="Select a Type" @change="changeQuestionType" />
                        <!-- <InputText id="methodname" type="text" v-model="lazyQuestion.name"  :class="{'borderless': true}"  @blur="updateName"  /> -->
                    <!-- <div class="p-error p-text-italic" v-for="error in nameErrors" :key="error"><small>{{error}}</small></div> -->
                </div>
                <div class="p-col p-field">
                    <span class="p-float-label">
                        <InputText id="questiondescription" type="text" v-model="lazyQuestion.description"  :class="{'borderless': true}" />
                        <label for="questiondescription">Description</label>
                    </span>
                    <!-- <div class="p-error p-text-italic" v-for="error in nameErrors" :key="error"><small>{{error}}</small></div> -->
                </div>
            </div>
            <div v-if="lazyQuestion.type === 'NUMBER'" class="p-grid p-col-12 p-fluid">
                <div class="p-col-4 p-field">
                    <span class="p-float-label">
                        <InputText id="minvalue" type="text" v-model="lazyQuestion.min"  :class="{'borderless': true}"  @blur="bb"  />
                        <label for="minvalue">Minimum value</label>
                    </span>
                </div>
                <div class="p-col-4 p-field">
                    <span class="p-float-label">
                        <InputText id="defaultvalue" type="text" v-model="lazyQuestion.default"  :class="{'borderless': true}"  @blur="cc"  />
                        <label for="defaultvalue">Default value</label>
                    </span>
                </div>
                <div class="p-col-4 p-field">
                    <span class="p-float-label">
                        <InputText id="maxvalue" type="text" v-model="lazyQuestion.max"  :class="{'borderless': true}"  @blur="dd"  />
                        <label for="maxvalue">Maximum value</label>
                    </span>
                </div>
            </div>
            <div v-if="lazyQuestion.options && lazyQuestion.options.length" class="p-grid p-py-5">
                <option-form v-for="(option, index) in lazyQuestion.options" :key="`option-${index}`" :option="option" @delete="deleteOption(option)" class="p-col-12" />
                <Button label="Add Option" class="p-button-text" @click="newOption" />

            </div>
        </form>
        <div v-else class="p-grid p-jc-center p-ai-center p-px-5" :style="cssProps">
            <i class="pi pi-question p-col-1" style="fontSize: 2rem"></i>
            <div class="p-col-11">
            <p><span class="p-text-bold">Question:</span> {{ question.name }}</p>
            <div class="p-d-flex p-jc-between p-mr-5 p-pr-5">
            <p><span class="p-text-bold">Key:</span> {{ question.key }}</p>
            <p><span class="p-text-bold">Type:</span> {{ questionType }}</p>
            </div>
            </div>
            <Divider />
            <div v-if="!question.options.length" class="p-d-flex p-jc-between">
                <p><span class="p-text-bold">Default value:</span> {{ question.default || 0 }}</p>
                <p v-if="question.min"><span class="p-text-bold">Minimum:</span> {{ question.min }}</p>
                <p v-if="question.max"><span class="p-text-bold">Maximum:</span> {{ question.max }}</p>
            </div>
            <template v-else>
                <div v-for="(option, index) in question.options" :key="index" class="p-field-checkbox p-col-12">
                    <Checkbox :id="index" name="option" :value="text" v-model="ss" />
                    <label :for="index"><span class="p-text-bold">Text:</span> '{{option.text}}'<span class="p-text-bold"> - Value:</span> '{{option.value}}'</label>
                </div>
            </template>
        </div>
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
            return this.questionTypesList.find(type => type.value === this.lazyQuestion.type).text
        },
        keyErrors () {
            return HandleValidationErrors(this.v$.lazyQuestion.key, this.errors.key)
        },
        nameErrors () {
            return HandleValidationErrors(this.v$lazyQuestion.name, this.errors.name)
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
            this.lazyQuestion.type = e.value
            const typesWithOptions = ['RADIO', 'CHECKBOX']
            if (typesWithOptions.includes(e.value) && !this.lazyQuestion.options.length) {
                this.lazyQuestion.options = [
                    { text: 'option 1', value: 'value' },
                    { text: 'option 2', value: 'value' }
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
