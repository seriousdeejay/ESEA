import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import IdleVue from 'idle-vue'
// import Vuelidate from 'vuelidate'
import Primevue from 'primevue/config'

import 'primevue/resources/themes/saga-blue/theme.css' // theme
import 'primevue/resources/primevue.min.css' // core css
import 'primeicons/primeicons.css' // icons
import 'primeflex/primeflex.css' // CSS Utility Library

import Menubar from 'primevue/menubar'
import Menu from 'primevue/menu'
import Card from 'primevue/card'
import Button from 'primevue/button'
import InputText from 'primevue/inputtext'
import Password from 'primevue/password'

// const eventsHub = createApp

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresLogin)) {
      if (!store.getters.loggedIn) {
        next({ name: 'login' })
      } else {
        next()
      }
    } else {
      next()
    }
  })

const app = createApp(App).use(store).use(router).use(Primevue).use(IdleVue, { idleTime: 5000, store }) // after 10sec idle

app.component('Menubar', Menubar)
app.component('Menu', Menu)
app.component('Card', Card)
app.component('Button', Button)
app.component('InputText', InputText)
app.component('Password', Password)

app.mount('#app')
