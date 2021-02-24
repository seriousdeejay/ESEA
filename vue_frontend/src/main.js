import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import IdleVue from 'idle-vue'
// import Vuelidate from 'vuelidate'
import Primevue from 'primevue/config'
import ToastService from 'primevue/toastservice'

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
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'
import ColumnGroup from 'primevue/columngroup' // optional for column grouping
import Paginator from 'primevue/paginator'
import Toolbar from 'primevue/toolbar'
import Dialog from 'primevue/dialog'
import Textarea from 'primevue/textarea'
import Toast from 'primevue/toast'
import SelectButton from 'primevue/selectbutton'
import Divider from 'primevue/divider'
import TabView from 'primevue/tabview'
import TabPanel from 'primevue/tabpanel'
import ToggleButton from 'primevue/togglebutton'
import DataView from 'primevue/dataview'
// const eventsHub = createApp

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresLogin)) {
      if (!store.getters['authentication/loggedIn']) {
        next({ name: 'login' })
      } else {
        next()
      }
    } else {
      next()
    }
  })

const app = createApp(App).use(store).use(router).use(Primevue).use(ToastService).use(IdleVue, { idleTime: 5000, store }) // after 10sec idle

app.component('Menubar', Menubar)
app.component('Menu', Menu)
app.component('Card', Card)
app.component('Button', Button)
app.component('InputText', InputText)
app.component('Password', Password)
app.component('DataTable', DataTable)
app.component('Column', Column)
app.component('ColumnGroup', ColumnGroup)
app.component('Paginator', Paginator)
app.component('Toolbar', Toolbar)
app.component('Dialog', Dialog)
app.component('Textarea', Textarea)
app.component('Toast', Toast)
app.component('SelectButton', SelectButton)
app.component('Divider', Divider)
app.component('TabView', TabView)
app.component('TabPanel', TabPanel)
app.component('ToggleButton', ToggleButton)
app.component('DataView', DataView)

app.mount('#app')
