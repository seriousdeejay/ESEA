<template>
    <div class="methods">
        <h1>Methods Overview</h1>
        <Button label="Method Wizard" @click="goToMethodCreate" />
        <Toast position="top-right"/>
        <div class="card p-m-5 p-shadow-2">
            <my-methods :columns="columns" selection-enabled></my-methods>
        </div>
    </div>
    <!-- <Dialog v-model:visible="methodDialog" :style="{width: '450px'}" header="Method Details" :modal="true" class="p-fluid">
        <div class="p-field">
            <label for="name">Name</label>
            <InputText id="name" v-model.trim="method.name" required="true" autofocus :class="{'p-invalid': submitted && !method.name}"
            @blur="updateMethodForm({ name: $event.target.value })" />
            <small class="p-error" v-if="submitted && !method.name">Name is required.</small>
        </div>
        <div class="p-field">
            <label for="description">Description</label>
            <Textarea id="description" v-model="method.description" required="true" rows="3" cols="20"
            @blur="updateMethodForm({ description: $event.target.value })" />
        </div>
        <div class="p-field">
            <label for="ispublic">Should this method be public? </label>
            <SelectButton id="ispublic" v-model="method.ispublic" required="true" :options="ispublicbool"
            @blur="updateMethodForm({ ispublic: $event.target.value })" />
        </div>
        <template #footer>
            <Button label="Cancel" icon="pi pi-times" class="p-button-text" @click="hideDialog"/>
            <Button label="Save" icon="pi pi-check" class="p-button-text" @click="saveMethod" :disabled="!method.name" />
        </template>
    </Dialog> -->
</template>

<script>
import { mapActions, mapState } from 'vuex'
import MyMethods from '../../components/MyMethods'
export default {
    components: {
        MyMethods
    },
    data () {
        return {
            columns: [
                { field: 'ispublic', header: 'public' },
                { field: 'name', header: 'Name' },
                { field: 'description', header: 'Description' },
                { field: 'surveys.length', header: 'Surveys' },
                { field: 'networks.length', header: 'Networks' },
                { field: 'organisations.length', header: 'Organisations' }
                ]
        }
    },
    computed: {
        ...mapState('method', ['method'])
    },
    methods: {
        ...mapActions('method', ['createMethod']),
        async goToMethodCreate () {
            await this.createMethod({})
            this.$router.push({ name: 'method-create', params: { id: this.method.id } })
        }
    }
}
</script>
