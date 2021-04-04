import { createStore } from 'vuex'
import VuexPersistance from 'vuex-persist'
import authentication from './modules/authentication'
import general from './modules/general'
import user from './modules/user'
import network from './modules/network'
import organisation from './modules/organisation'
import method from './modules/method/method'
import survey from './modules/method/survey'
import topic from './modules/method/topic'
import question from './modules/method/question'
import campaign from './modules/campaign'
import eseaAccount from './modules/esea_account'
import surveyResponse from './modules/method/survey/survey_response'
import surveyResults from './modules/method/survey/survey_results'
const vuexLocalStorage = new VuexPersistance({
  storage: window.localStorage
//  ... can be used to use local storage
})

export default createStore({
  modules: {
    authentication,
    general,
    user,
    network,
    organisation,
    method,
    survey,
    topic,
    question,
    campaign,
    eseaAccount,
    surveyResponse,
    surveyResults
  },
  plugins: [vuexLocalStorage.plugin]
})
