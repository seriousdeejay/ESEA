<template>
    <div class="p-grid p-col-12">
        <div class="p-col-6">
        <InputText id="optiontext" type="text" v-model="lazyOption.text" placeholder="Option text" :class="{'borderless': true}" @blur="dd"  />
        </div>
        <div class="p-col-5">
        <InputText id="optionvalue" type="text" v-model="lazyOption.value" placeholder="Option text" :class="{'borderless': true}" @blur="dd"  />
        </div>
        <Button icon="pi pi-trash" class="p-col p-button-danger p-button-text" @click="deleteOption" />
    </div>
</template>

<script>
import { required } from '../../utils/validators'
import useVuelidate from '@vuelidate/core'

export default {
    props: {
        option: {
            type: Object,
            required: true
        }
    },
    data () {
        return {
            lazyOption: this.option
        }
    },
    watch: {
        option (val) {
            this.lazyOption = val
        },
        lazyOption (val) {
            if (val !== this.option) {
                this.update()
            }
        }
    },
    setup: () => ({ v$: useVuelidate() }),
    validations: {
        lazyOption: {
            text: { required },
            value: { required }
        }
    },
    methods: {
        update () {
            this.$emit('update', this.lazyOption)
        },
        deleteOption () {
            this.$emit('delete')
        }
    }
}
</script>
