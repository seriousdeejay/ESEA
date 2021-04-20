<template>
        <form ref="form" v-if="active" class="p-grid p-px-5 p-pt-5" :style="cssProps"  >
            <div class="p-grid p-col-12 p-fluid">
                <div class="p-col-3 p-field">
                    <span class="p-float-label">
                        <InputText id="calculationkey" ref="keyinput" type="text" v-model="lazyIndirectIndicator.name"  :class="{'borderless': nameErrors.length}"  @blur="updateName"  />
                        <label for="calculationkey">Key</label>
                    </span>
                    <div class="p-error p-text-italic" v-for="error in nameErrors" :key="error"><small>{{error}}</small></div>
                </div>
                <div class="p-col p-field">
                    <span class="p-float-label">
                        <InputText id="calculationdescription" type="text" v-model="lazyIndirectIndicator.description" />
                        <label for="calculationdescription">Description</label>
                    </span>
                </div>
                <div class="p-col-12 p-field">
                    <span class="p-float-label">
                        <InputText id="calculationformula" ref="calculationinput" type="text" v-model="lazyIndirectIndicator.formula" :class="{'borderless': formulaErrors.length}" @blur="updateFormula" />
                        <label for ="calculationformula">Formula</label>
                    </span>
                    <div class="p-error p-text-italic" v-for="error in formulaErrors" :key="error"><small>{{error}}</small></div>
                </div>
            </div>
        </form>
        <div v-else class="p-px-5 p-grid p-ai-center" :style="cssProps">
            <i class="pi pi-percentage p-col-1" style="fontSize: 2rem"></i>
            <div class="p-col-11">
            <p><span class="p-text-bold">Indirect Indicator:</span> {{ indirectIndicator.name }}</p>
            <p><span class="p-text-bold">Formula:</span> {{ indirectIndicator.formula }}</p>
            </div>
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
                props['background-color'] = 'white'
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
                if (this.v$.$invalid) { return }
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
