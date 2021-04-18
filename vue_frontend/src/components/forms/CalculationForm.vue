<template>
    <form>

    </form>
</template>

<script>
import useVuelidate from '@vuelidate/core'
import HandleValidationErrors from '../../utils/HandleValidationErrors'
import { maxLength } from '../../utils/validators'
export default {
    props: {
        indirectIndicator: {
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
            tab: null,
            lazyIndirectIndicator: { ...this.indirectIndicator}
        }
    },
    
    computed: {
        ...mapGetters('indirectIndicator', ['getValidIndirectIndicatorNumber']),
        nameErrors () {
            return HandleValidationErrors(
                this.v$.lazyIndirectIndicator.name,
                this.errors.name
            )
        },
        formulaErrors () {
            return HandleValidationErrors(
                this.v$.lazyIndirectIndicator.formula,
                this.errors.formula
            )
        }
    },
    watch: {
        indirectIndicator (val) {
            if (!isEqual(this.lazyIndirectIndicator, val)) {
                if (this.lazyIndirectIndicator.formula !== val.formula) {
                    this.$refs.calculationInput.focus()
                }
                this.lazyIndirectIndicator = { ...val }
            }
        },
        lazyIndirectIndicator: {
            deep: true,
            handler (val) {
                if (isEqual(this.indirectIndicator, val)) return
                this.$emit('input', val)
            }
        },
        active (val) {
            if (!val) {
                this.v$.$touch()
            } else {
                this.$nextTick(() => this.$refs.input && this.$refs.input.focus());
            }
        }
    },
    created () {
        this.initialize()
    },
    setup: () => ({ v$: useVuelidate() }),
    validations: {
        lazyIndirectIndicator: {
            name: { required, maxLength: maxLength(255) },
            formula: { required }
        }
    },
    methods: {
        initialize () {
            if (!this.lazyIndirectIndicator.name) {
                this.lazyIndirectIndicator = `indirect_indicator_${this.getValidIndirectIndicatorNumber}`
            }
        },
        updateName () {
            this.v$.lazyIndirectIndicator.formula.$touch()
        },
        updateFormula () {
            this.v$.lazyIndirectIndicator.formula.$touch()
        }
    }
}
</script>