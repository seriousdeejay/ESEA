<template>
    <form ref="form" class="p-grid p-fluid p-input-filled p-py-5">
        <div class="p-col-12 p-field">
            <span class="p-float-label">
            <InputText id="surveyname" type="text" v-model="lazySurvey.name" @blur="updateName" />
            <label for="surveyname">Survey Name</label>
            </span>
        </div>
        <div class="p-grid p-col-12 p-m-0 p-p-0">
            <div class="p-col-8">
                <span class="p-float-label">
                <InputText id="surveystakeholders" type="text" v-model="lazySurvey.stakeholder" @blur="updateStakeholder" />
                <label for="surveystakeholders">Stakeholder Group</label>
                </span>
            </div>
            <div class="p-col-4">
                <span class="p-float-label">
                    <InputNumber id="surveyresponserate" suffix="%" :min="0" :max="100" v-model="lazySurvey.rate" />
                    <label for="surveyresponserate">Response Rate</label>
                </span>
            </div>
        </div>
        <Divider />
        <!-- <tree-select v-model="items"></tree-select> -->
        <div class="p-grid p-col-12 p-mx-0 p-px-0 p-field">
                 <div class="p-col-4">
                    <!-- <span class="p-float-label">
                        <InputText id="questionkey" type="text" v-model="dd"  :class="{'borderless': keyErrors.length}"  @blur="questionKeyFilter" :disabled="!active" />
                        <label for="questionkey">Question Key</label>
                    </span>
                    <div class="p-error p-text-italic" v-for="error in keyErrors" :key="error"><small>{{error}}</small></div> -->
                </div>
        </div>
    </form>
</template>
<script>
import useVuelidate from '@vuelidate/core'
import { required, maxLength } from '../../utils/validators'
import HandleValidationErrors from '../../utils/HandleValidationErrors'
import { isEqual } from 'lodash'
// import TreeSelect from 'primevue/treeselect'

export default {
    components: {
        // TreeSelect
    },
    props: {
        survey: {
            type: Object,
            required: true
        },
        items: {
            type: Array,
            required: true
        },
        stakeholders: {
            type: Array,
            required: true
        },
        errors: {
            type: Object,
            required: true
        }
    },
    data () {
        return {
            lazySurvey: { ...this.survey }
        }
    },
    computed: {
        // items () {
        //     const data = getMethodItems(this.methodTopics,
		// 		this.subTopics,
		// 		this.topicQuestions,
		// 		this.topicIndirectIndicators)

        //     for (const topic of data) {
        //         topic.label = topic.name
        //         for (const subtopic of topic.children) {
        //             subtopic.label = subtopic.name
        //             for (const indicator of subtopic.children) {
        //                 indicator.label = indicator.key
        //                 if (indicator.objType === 'calculation') {
        //                     indicator.icon = 'pi pi-percentage'
        //                 } else {
        //                     indicator.icon = 'pi pi-pencil'
        //                 }
        //             }
        //         }
        //     }
        //     return data
        nameErrors () {
            return HandleValidationErrors(
                this.v$.lazySurvey.name
            )
        },
        stakeholderErrors () {
            return HandleValidationErrors(
                this.v$.lazySurvey.stakeholder
            )
        }
    },
    watch: {
        survey (val) {
            if (!isEqual(this.lazySurvey, val)) {
                this.lazySurvey = { ...val }
            }
        },
        lazySurvey: {
            handler (val) {
                setTimeout(() => {
                    console.log('check')
                    if (this.v$.invalid) { return }
                    if (isEqual(this.topic, this.lazySurvey)) { return }
                    console.log('check')
                    console.log('++', this.lazySurvey)
                    this.$emit('input', this.lazySurvey)
                }, 200)
            },
            deep: true
        }
    },
    setup: () => ({ v$: useVuelidate() }),
    validations: {
        lazySurvey: {
            name: { required, maxLength: maxLength(120) },
            stakeholder: { required }
        }
    },
    methods: {
        updateName () {
            this.v$.lazySurvey.name.$touch()
        },
        updateStakeholder () {
            this.v$.lazySurvey.stakeholder.$touch()
        }
    }
}
</script>
