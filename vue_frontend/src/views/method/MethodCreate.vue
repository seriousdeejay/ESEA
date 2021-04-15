<template>
<h1>Hi</h1>
<div class="p-grid">
    <div class="p-fixed" style="200px">
        {{method}}
    </div>
    <div class="p-col">
        <method-form :method="method" @input="updateMethod($event)" />
    </div>
</div>
<!-- Method creation wizard -->
</template>

<script>
import { mapState, mapActions } from 'vuex'
import MethodForm from '../../components/forms/MethodForm'

export default {
    components: {
        MethodForm
    },
    data () {
        return {
            updateToolbar: 0
        }
    },
    computed: {
        ...mapState('method', ['method', 'error'])
    },
    created () {
        this.initialize()
    },
    methods: {
        ...mapActions('method', ['fetchMethod', 'updateMethod', 'saveMethod']),
        async initialize () {
            const methodId = parseInt(this.$route.params.id, 10)
            if (this.method.id !== methodId) {
                await this.fetchMethod({
                    id: methodId
                })
                // if (this.error) { this.$router.push({ name: 'methods' }) }
            }
        }
    }
}
</script>
