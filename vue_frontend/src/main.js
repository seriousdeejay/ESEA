import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
// import Vuelidate from 'vuelidate'
import Primevue from 'primevue/config'

import 'primevue/resources/themes/saga-blue/theme.css' // theme
import 'primevue/resources/primevue.min.css' // core css
import 'primeicons/primeicons.css' // icons
import 'primeflex/primeflex.css' // CSS Utility Library

import Menubar from 'primevue/menubar'
import Card from 'primevue/card'
import Button from 'primevue/button'

const app = createApp(App).use(store).use(router).use(Primevue)

app.component('Menubar', Menubar)
app.component('Card', Card)
app.component('Button', Button)

app.mount('#app')
