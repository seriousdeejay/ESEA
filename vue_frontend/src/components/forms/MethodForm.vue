<template>
    <form ref="form"  class="p-fluid p-p-5 p-input-filled p-inputtext-lg" @click="tester()"> <!-- @submit.prevent="!v$.$invalid" -->
        <div class=" p-mb-5">
            <span class="p-float-label">
                <InputText id="methodname" type="text" v-model="lazyMethod.name"  :class="{'borderless': nameErrors.length}" @blur="updateName"  />
                <label for="methodname"><span class="p-text-bold" style="font-size: 18px;">Method Name</span></label>
            </span>
            <div class="p-error p-text-italic p-pt-1" v-for="error in nameErrors" :key="error">{{error}}</div>
        </div>
        <div>
            <span class="p-float-label">
                <InputText id="methoddescription" type="text" v-model="lazyMethod.description" :class="{'borderless': descriptionErrors.length}" @blur="updateDescription" />
                <label for="methoddescription"><span class="p-text-bold" style="font-size: 16px;">Method Description</span></label>
            </span>
            <div class="p-error p-text-italic p-pt-1" v-for="error in descriptionErrors" :key="error">{{error}}</div>
        </div>
    </form>
</template>

<script>
import { isEqual } from 'lodash'
import useVuelidate from '@vuelidate/core'
import { required, minLength, maxLength } from '../../utils/validators'
import HandleValidationErrors from '../../utils/HandleValidationErrors'

export default {
    props: {
        method: {
            type: Object,
            default: () => ({})
        },
        errors: {
            type: Object,
            default: () => ({})
        }
    },
    data () {
        return {
            lazyMethod: { id: this.method.id, name: this.method.name, description: this.method.description }
        }
    },
    computed: {
        nameErrors () {
            return HandleValidationErrors(
                this.v$.lazyMethod.name,
                this.errors.name
                )
        },
        descriptionErrors () {
            return HandleValidationErrors(
                this.v$.lazyMethod.description,
                this.errors.description
            )
        }
    },
    watch: {
        method (val) {
            if (!isEqual(this.lazyMethod.name, val.name) && !isEqual(this.lazyMethod.description, val.description)) {
                this.lazyMethod = { id: val.id, name: val.name, description: val.description }
            }
        },
        'v$.lazyMethod.$invalid': function () {
            if (this.v$.lazyMethod.$invalid) { return }
            if (isEqual(this.lazyMethod.name, this.method.name) && isEqual(this.lazyMethod.description, this.method.description)) {
                return
            }
            this.$emit('input', this.lazyMethod)
        }
    },
    setup: () => ({ v$: useVuelidate() }),
    validations: {
        lazyMethod: {
            id: { required },
            name: { required, minLength: minLength(2), maxLength: maxLength(255) },
            description: { required }
        }
    },
    methods: {
        updateName () {
            this.v$.lazyMethod.name.$touch()
        },
        updateDescription () {
            this.v$.lazyMethod.description.$touch()
        },
        tester () {
            console.log('works!')
        }
    }
}
        // lazyMethod: {
        //     deep: true,
        //     handler: function (val) {
        //         console.log('lll', val, this.method)
        //         console.log('>>', val)
        //         if (this.v$.lazyMethod.$invalid) {
        //             console.log('invalid!', this.v$.lazyMethod.$invalid, this.lazyMethod)
        //             return
        //         }
        //         if (isEqual(this.method, val)) {
        //             console.log('equal!')
        //             return
        //         }
        //         console.log('>>', val)
        //         this.$emit('input', val)
        //     }
        // }
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
