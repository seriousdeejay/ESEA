<template>
<div class="p-grid p-col-12 p-d-flex p-ai-center p-jc-center p-fluid">
    <div class="p-col-6">
        <span class="p-float-label">
            <InputText id="optiontext" type="text" v-model="lazyOption.text" :class="{'borderless': true}"  @blur="dd"  />
            <label for="questiondescription">Option text</label>
        </span>
    </div>
    <div class="p-col-5">
        <span class="p-float-label">
            <InputText id="optionvalue" type="text" v-model="lazyOption.value" :class="{'borderless': true}"  @blur="dd"  />
            <label for="optionvalue">Option value</label>
        </span>
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
