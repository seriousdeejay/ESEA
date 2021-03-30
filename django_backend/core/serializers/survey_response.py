from rest_framework import serializers

from ..models import SurveyResponse, QuestionResponse, QuestionOption, DirectIndicator
from .question_response import QuestionResponseSerializer
from .user_organisation import UserOrganisationSerializer

class SurveyResponseSerializer(serializers.ModelSerializer):
    question_responses = QuestionResponseSerializer(many=True)
    user_organisation = UserOrganisationSerializer(read_only=True)

    class Meta:
        model = SurveyResponse
        fields = '__all__'
        read_only_fields = ['survey', 'user_organisation', 'token']
    
    def create(self, validated_data):
        question_responses = validated_data.pop('question_responses')
        survey = validated_data.pop('survey')
        direct_indicators = DirectIndicator.objects.filter(question__survey=survey)
        for direct_indicator in direct_indicators:
            question_response = QuestionResponse.objects.create(survey_response= survey, direct_indicator_id=direct_indicator)

        # surveys.question.direct_indicators
        survey_response = SurveyResponse.objects.create(**validated_data)
        # survey_response.save_question_responses(question_responses)
        return survey_response

    def update(self, survey_response, validated_data):
        print('d')
        question_responses = validated_data.pop('question_responses')
        print('////', question_responses)
        question_responses_dict = dict((i.id, i) for i in survey_response.question_responses.all())
        print(question_responses_dict)
        for item_data in question_responses:
            if 'id' in item_data:
                question_response = QuestionResponse.objects.get(id=item_data['id']) #question_responses_dict.pop(item_data['id'])
                
                for key in item_data.keys():
                    if key == 'values':
                        question_response.values.clear()
                        for answer in item_data[key]:
                            print(answer)
                            question_response.values.add(answer)
                    else:
                        setattr(question_response, key, item_data[key])
                question_response.save()
                print(question_response)
                
        # raise_errors_on_nested_writes('update', self, validated_data)
        # print(validated_data)
        # survey_response.question_responses.set = validated_data.get('question_responses', survey_response.question_responses)
        # for attr, value in validated_data.items():
        #     if attr == 'question_responses':
        #         for item in value:
        #             print('--->', item, item['direct_indicator_id'], item['values'])
        #             for answer in item['values']:
        #                 questionresponse, _ =  QuestionResponse.objects.get_or_create(id=item['id'])
        #                 print('||', questionresponse)
        #             # QuestionOption.objects.get(item['values'])
        #         # for attr, value in value.items():
        #         #     print(attr)
        #         # print('yeay!', value)
        #     # print('----', attr)
        #     else:
        #         setattr(survey_response, attr, value)
        # survey_response.save()
        #print(survey_response.question_responses.all())
        

        return survey_response
    #     survey_response.finished = validated_data.get('finished', survey_response.finished)
    #     print('pppp', validated_data)
    #     survey_response.save()
    #     print(vars(survey_response))
    #     print('zzzzz', validated_data.get('question_responses', survey_response.question_responses))
    #     #question_responses = validated_data.get('question_responses', [])
    #    # survey_response.save_question_responses(question_responses)
    #     return survey_response

class SurveyResponseCalculationSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    topic = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField(read_only=True)
    key = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    formula = serializers.CharField(read_only=True)
    calculation = serializers.CharField(read_only=True)
    value = serializers.CharField(read_only=True)
    responses = serializers.ListField(child=serializers.CharField(read_only=True))

    