<template>
    <my-methods :columns=columns network-methods selection-enabled></my-methods>
</template>
<script>
import MyMethods from '../../components/MyMethods'
export default {
    components: {
        MyMethods
    },
    data () {
        return {
            columns:
            [
                { field: 'name', header: 'Name' },
                { field: 'description', header: 'Description' },
                { field: 'surveys.length', header: 'Surveys' }
            ]
        }
    }
}
</script>
