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
            lazyValue: [],
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
        // value (val) {
            // if (val !== this.lazyValue) {
                // console.log('ddd', val)
                // console.log(this.value)
                // console.log(this.lazyValue)
                // this.lazyValue = this.type === this.questionTypes.CHECKBOX ? this.splitValue(val) : val
            // }
        // },
        lazyValue (val) {
            // console.log(this.lazyValue)

            // if (this.type === this.questionTypes.RADIO)

            // if (this.type === this.questionTypes.CHECKBOX) {
                // console.log('==========', val)
                // const checked = this.splitValue(this.value)
                // console.log('>>>>>>', checked)
                // if (!val.length) {
                    // this.lazyValue = checked
                    // console.log(this.lazyValue)
                //    return
                // }
                // if (val === checked) return
			// }
            console.log('mmm', val)
            //
            if ((val === 'undefined') || (val === this.value)) {
                console.log('dd')
                return
            }
            if (!Array.isArray(val)) {
               this.$emit('input', [val])
               return
            }

            if (typeof (val || val[0]) === 'undefined') {
                console.log('zz')
                return
            }
            console.log('sss', val)
			this.$emit('input', val)
        }
    },
    created () {
        if (this.type === this.questionTypes.RADIO) {
            console.log('----', this.value)
            try {
                this.lazyValue = this.value[0]
            } catch {
                this.lazyValue = null
        }
        console.log(this.lazyValue)
        } else {
        this.lazyValue = this.value
        }
        // console.log(this.options)
        // console.log(this.value)
        // console.log(this.lazyValue)
        // if (this.type === this.questionTypes.CHECKBOX) {
            // this.lazyValue = this.splitValue(this.lazyValue)
        // }
    }
    // methods: {
    //     splitValue (value) {
    //         console.value('sss', value)
    //         return value ? value.split(',') : value
    //     }
    // }
}
</script>
