<template>
    <div class="p-grid p-d-flex p-ai-center" :style="cssProps">
        <i class="pi pi-percentage p-col-1 p-text-center" style="fontSize: 3rem; color: grey;"></i>
        <form ref="form" class="p-grid p-col-11 p-pt-5 p-pr-5 p-fluid p-input-filled">
            <div class="p-grid p-col-12 p-mx-0 p-px-0 p-pt-5 p-field">
                <div class="p-col-4">
                    <span class="p-float-label">
                        <InputText id="calculationkey" ref="keyinput" type="text" v-model="lazyIndirectIndicator.key"  :class="{'borderless': nameErrors.length}"  @blur="updateName" :disabled="!active" />
                        <label for="calculationkey">Key</label>
                    </span>
                    <div class="p-error p-text-italic" v-for="error in nameErrors" :key="error"><small>{{error}}</small></div>
                </div>
                <div class="p-col-8">
                    <span class="p-float-label">
                        <InputText id="calculationame" type="text" v-model="lazyIndirectIndicator.name" :disabled="!active" />
                        <label for="calculationname">Name</label>
                    </span>
                </div>
            </div>
            <div v-if="active" class="p-col-12 p-field">
                <span class="p-float-label">
                    <InputText id="calculationdescription" type="text" v-model="lazyIndirectIndicator.description" :disabled="!active" />
                    <label for="calculationdescription">Description</label>
                </span>
            </div>
            <div class="p-col-12 p-field">
                <span class="p-float-label">
                    <InputText id="calculationformula" ref="calculationinput" type="text" v-model="lazyIndirectIndicator.formula" :class="{'borderless': formulaErrors.length}" @blur="updateFormula" :disabled="!active" />
                    <label for ="calculationformula">Formula</label>
                </span>
                <div class="p-error p-text-italic p-pt-1" v-for="error in formulaErrors" :key="error">{{error}}</div>
            </div>
        </form>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
import useVuelidate from '@vuelidate/core'
import HandleValidationErrors from '../../utils/HandleValidationErrors'
import { required, maxLength } from '../../utils/validators'
import { isEqual, cloneDeep } from 'lodash'

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
    setup: () => ({ v$: useVuelidate() }),
    validations: {
        lazyIndirectIndicator: {
            name: { required, maxLength: maxLength(255) },
            formula: { required }
        }
    },
    data () {
        return {
            tab: null,
            lazyIndirectIndicator: { ...this.indirectIndicator } // cloneDeep(this.indirectIndicator) || {} //
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
        },
        cssProps () {
            const props = { border: '1px solid lightgrey' }
            if (this.active) {
                props.border = '2px solid #9ecaed'
                props['background-color'] = '#f7f7f7' // '#d0dfff' // '#E1E8ED' // '#DFE3EE' // '#CCD6DD' // '#E1E8ED' // '#cfe0e8' // '#fbfbfb'
            }
            return props
        }
    },
    watch: {
        indirectIndicator (val) {
            if (!isEqual(this.lazyIndirectIndicator, val)) {
                // if (this.lazyIndirectIndicator.formula !== val.formula) {
                //     this.$refs.calculationinput.focus()
                // }
                this.lazyIndirectIndicator = cloneDeep(val) // { ...val }
            }
        },
        lazyIndirectIndicator: {
            handler (val) {
                setTimeout(() => {
                if (this.v$.lazyIndirectIndicator.$invalid) { return }
                if (isEqual(this.indirectIndicator, val)) { return }
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
        if (!this.lazyIndirectIndicator.name) {
        }
    },
    created () {
        this.initialize()
    },
    methods: {
        initialize () {
            if (!this.lazyIndirectIndicator.key) {
                this.lazyIndirectIndicator.key = `indirect_indicator_${this.getValidIndirectIndicatorNumber}`
            }
            if (!this.lazyIndirectIndicator.name) {
                this.lazyIndirectIndicator.name = `indirect_indicator_${this.getValidIndirectIndicatorNumber}`
            }
            if (!this.lazyIndirectIndicator.formula) {
                this.lazyIndirectIndicator.formula = ''
            }
        },
        updateName () {
            this.v$.lazyIndirectIndicator.name.$touch()
        },
        updateFormula () {
            this.v$.lazyIndirectIndicator.formula.$touch()
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
