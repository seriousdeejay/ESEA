<template>
    <div class="p-p-3 p-my-3" style="border: 1px solid lightgrey;">
        <InputNumber v-if="type === questionTypes.NUMBER" v-model="lazyValue" :disabled="readonly" required/>
        <InputText v-if="type === questionTypes.TEXT" type="text" v-model="lazyValue" :disabled="readonly" required/>

        <div v-if="type === questionTypes.CHECKBOX">
            <div v-for="(option, index) in options" :key="`${index}-option`" class="p-field-checkbox">
                <Checkbox :id="`${index}-option`" name="option" :value="option[optionValueKey]" v-model="lazyValue" :disabled="readonly" required/>
                <label :for="`${index}-option`" class="p-text-left">{{option[optionTextKey]}}</label>
            </div>
        </div>

        <div v-if="type === questionTypes.RADIO">
            <div v-for="(option, index) in options" :key="`${index}-option`" class="p-field-radiobutton">
                <RadioButton :id="`${index}-option`" name="option" :value="option[optionValueKey]" v-model="lazyValue" :disabled="readonly" required/>
                <label :for="`${index}-option`" class="p-text-left">{{option[optionTextKey]}}</label>
            </div>
        </div>
    </div>
</template>

<script>
    import { QUESTION_TYPES } from '../../utils/constants'

export default {
    model: {
        prop: 'value',
        event: 'input'
    },
    props: {
        value: {
            type: [String, Number, Array],
            default: undefined
        },
        required: {
            type: Boolean,
            default: false
        },
        type: {
            type: String,
            default: 'text'
            // validator: v => Object.values(QUESTION_TYPES).includes(v)
        },
        options: {
            type: Array,
            default: () => ([])
        },
        optionTextKey: {
            type: String,
            default: 'text'
        },
        optionValueKey: {
            type: String,
            default: 'value'
        },
        readonly: {
            type: Boolean,
            default: false
        },
        checkanswerrequired: {
            type: Boolean,
            default: undefined
        }
    },
    data () {
        return {
            lazyValue: this.value,
            completedBool: this.checkanswerrequired,
            questionTypes: QUESTION_TYPES
        }
    },
    computed: {
        // parsedType() {
		// 	return this.type.toLowerCase();
		// },
    },
    watch: {
        completedBool (val) {
        },
        value (val) {
            if (val !== this.lazyValue) {
                this.lazyValue = this.type === this.questionTypes.CHECKBOX ? this.splitValue(val) : val
            }
        },
        lazyValue (val) {
            if (val === this.value) return
            if (this.type === this.questionTypes.CHECKBOX) {
                const checked = this.splitValue(this.value)
                if (!val.length) {
                    this.lazyValue = checked
                    return
                }
                if (val === checked) return
			}
			this.$emit('input', `${val}`)
        }
        // checkanswerrequired: function (val, oldval) {
        //     console.log('hello')
        //     if (this.checkanswerrequired) {
        //         console.log('goodday')
        //     this.$emit('completed', this.completedBool)
        //     }
        // }
    },
    created () {
        if (this.type === this.questionTypes.CHECKBOX) {
            this.lazyValue = this.splitValue(this.lazyValue)
        }
    },
    methods: {
        splitValue (value) {
            return value ? value.split(',') : value
        }
    }
}
</script>
