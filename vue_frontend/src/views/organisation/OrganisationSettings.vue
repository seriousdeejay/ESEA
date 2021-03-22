<template>
    <div class="p-px-5" style="width: 500px">
        <div class="p-fluid p-text-left p-my-5">
            <div class="p-field">
                <label for="name">Name</label>
                <InputText id="name" v-model.trim="organisation.name" required="true" autofocus :class="{'p-invalid': submitted && !organisation.name}" class="p-text-italic" />
                <small class="p-error" v-if="!organisation.name">Name is required.</small>
            </div>
            <div class="p-field">
                <label for="description">Description</label>
                <Textarea id="description" v-model="organisation.description" class="p-text-italic" required="false" rows="3" cols="20" />
            </div>
                <div class="p-field">
                <label for="ispublic">Should this orgnaisation be public? </label>
                <SelectButton id="ispublic" v-model="boolChoice" :options="ispublicbool" optionLabel="name" @focus="ispublicDialog = true" :disabled="true" class="p-mb-3" />

                <small class="p-text-italic">*Public organisations are visible to anyone. Explicitly granted access is still required for certain operations.</small>
            </div>
        </div>
        <div class="p-d-flex p-jc-between">
                <Button label="Save Network Details" class="p-button-primary" @click="editNetwork" :disabled="false" />
                <Button label="Delete Network" class="p-button-danger" @click="deleteNetworkDialog = true" />
            </div>
   </div>

    <Dialog v-model:visible="ispublicDialog" :style="{width: '450px'}" header="Premium required" :modal="true">
        <i class="pi pi-star p-mr-3" style="font-size: 1.5rem" />
        <span>You need premium to make your organisation private.</span>
        <template #footer>
            <Button label="No thanks" icon="pi pi-times" class="p-button-text" @click="ispublicDialog = false"/>
            <Button label="What's Premium?" icon="pi pi-question" class="p-button-text" @click="ispublicDialog = false" />
        </template>
    </Dialog>

    <Dialog v-if="organisation" v-model:visible="deleteOrganisationDialog" :style="{width: '450px'}" header="Confirm" :modal="true">
        <div class="confirmation-content">
            <i class="pi pi-exclamation-triangle p-mr-3" style="font-size:1.5rem" />
            <span>Are you sure you want to delete <b>{{organisation.name}}</b>?</span>
        </div>
        <template #footer>
            <Button label="No" icon="pi pi-times" class="p-button-text" @click="deleteOrganisationDialog = false"/>
            <Button label="Yes" icon="pi pi-check" class="p-button-text" @click="removeOrganisation()" />
        </template>
    </Dialog>
</template>
<script>
import { mapState, mapActions } from 'vuex'
export default {
    data () {
        return {
            ispublicbool: [
                { name: 'Public', value: true },
                { name: 'Private', value: false }
            ],
            boolChoice: null,
            ispublicDialog: false,
            deleteOrganisationDialog: false
        }
    },
    computed: {
        ...mapState('organisation', ['organisation'])
    },
    created () {
        this.initialize()
    },
    methods: {
        ...mapActions('organisation', ['updateOrganisation', 'deleteOrganisation']),
        initialize () {
            this.boolChoice = { name: 'Public', value: this.organisation.ispublic }
        },
        async editOrganisation () {
            await this.updateOrganisation({})
            this.$toast.add({ severity: 'success', summary: 'Successful', detail: 'Organisation Updated', life: 3000 })
        },
        async removeOrganisation () {
            this.deleteOrganisationDialog = false
            await this.deleteOrganisation({ id: this.organisation?.id || 0 })
            this.$toast.add({ severity: 'success', summary: 'Succesful', detail: 'Organisation Deleted', life: 3000 })
            this.$router.push({ name: 'organisations' })
        }
    }
}
</script>
