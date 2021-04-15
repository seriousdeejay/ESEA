<template>
<h1>dd</h1>
    <form ref="form" width="100%" class="p-fluid" @submit.prevent="save">
         <div class="p-field ">
             <span class="p-float-label">
                <InputText id="myinput" type="text" v-model="lazyMethod.name" autofocus :class="{'p-invalid': submitted && !lazyMethod.name}" @blur="updateName" @focus="focuss"/>
                <label for="methodname">Name</label>
                <small class="p-error" v-if="submitted && !lazyMethod.name">A name is required.</small>
             </span>
         </div>
         <div class="p-field">
             <span class="p-float-label">
                 <InputText id="methoddescription" type="text" v-model="lazyMethod.description" :class="{'p-invalid': submitted && !lazyMethod.name}" @blur="updateDescription" />
                 <label for="methoddescription">Description</label>
                 <small class="p-error" v-if="submitted && !lazyMethod.description">A description is required.</small>
             </span>
         </div>
    </form>
</template>

<script>
import { isEqual } from 'lodash'
import { required, maxLength } from '../../utils/validators'
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
            lazyMethod: { ...this.method },
            focuss: false
        }
    },
    computed: {
        nameErrors () {
            return HandleValidationErrors(
                this.$v.lazyMethod.name,
                this.errors.name
                )
        },
        descriptionErrors () {
            return HandleValidationErrors(
                this.$v.lazyMethod.description,
                this.errors.description
            )
        }
    },
    watch: {
        method (val) {
            if (!isEqual(this.lazyMethod, val)) {
                this.lazyMethod = { ...val }
            }
        },
        lazyMethod: {
            deep: true,
            handler (val) {
                if (this.$v.$invalid) return
                if (isEqual(this.method, val)) return
                this.$emit('input', val)
            }
        }
    },
    methods: {
        updateName () {
            this.$v.lazyMethod.name.$touch()
        },
        updateDescription () {
            this.$v.lazyMethod.description.$touch()
        }
    },
    validations: {
        lazyMethod: {
            name: { required, laxLength: maxLength(255) },
            description: { required }
        }
    }

}
</script>
