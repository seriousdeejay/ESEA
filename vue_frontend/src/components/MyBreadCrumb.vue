<template>
    <BreadCrumb :home="home" :model="items" />
</template>
<script>
import BreadCrumb from 'primevue/breadcrumb'

export default {
    components: {
        BreadCrumb
    },
    props: {
    },
    data () {
        return {
            home: { icon: 'pi pi-home', to: '/' },
            items: []
        }
    },
    watch: {
        '$route' () {
            var breadcrumbList
            breadcrumbList = this.$route.meta.breadcrumb
            console.log(breadcrumbList)
            this.changeBreadCrumb(breadcrumbList)
        }
    },
    methods: {
        changeBreadCrumb (breadcrumbList) {
            // const realpath = this.$route.path
            const pathname = this.$route.name
            const paths = this.$route.path.split('/').slice(1)
            const breadcrumb = this.$route.meta.breadcrumb || {}
            console.log('===', breadcrumb)
            paths.forEach((path, i) => {
                if (breadcrumb[i]) {
                    if (!breadcrumb[i].label) {
                        // breadcrumb[i].label = path
                        breadcrumb[i] = { label: path, to: { name: pathname, params: { id: parseInt(path) } } }
                        console.log(breadcrumb[i])
                        // breadcrumb[i].to.params.id = path
                        // breadcrumb[i].label = path
                        // breadcrumb[i].to = realpath
                    }
                //         breadcrumb[i].label = path
                //         breadcrumb[i].to = path
                //     // breadcrumb[i] = breadcrumb[i].label ? breadcrumb[i].label : path
                }
            })
            console.log('}}}', breadcrumb)
            this.items = breadcrumb
            console.log(this.items)
        }
    }
}
</script>
