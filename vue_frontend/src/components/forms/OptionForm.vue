<template>
    <div class="p-grid p-col-12">
        <div class="p-col-6">
        <InputText id="optiontext" type="text" v-model="lazyOption.text" placeholder="Option text" :class="{'borderless': v$.lazyOption.text.$invalid}" />
        </div>
        <div class="p-col-5">
        <InputText id="optionvalue" type="number" v-model="lazyOption.value" placeholder="Option value" :class="{'borderless': v$.lazyOption.value.$invalid}" />
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
            if (this.v$.lazyQuestion.$invalid) { return }
            if (val !== this.option && val.text && val.value) {
                 this.$emit('update', this.lazyOption)
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
        deleteOption () {
            this.$emit('delete')
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
