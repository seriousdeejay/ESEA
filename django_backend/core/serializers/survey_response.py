from rest_framework import serializers

from ..models import SurveyResponse, QuestionResponse, QuestionOption, DirectIndicator, UserOrganisation
from .question_response import QuestionResponseSerializer
from .user_organisation import UserOrganisationSerializer

import random
import string

# class UserOrganisationField(serializers.RelatedField):
#     def to_representation(self, obj):
#         print('ddd', obj)
#         data = super(UserOrganisationSerializer).to_representation(obj)
#         return data

#     def to_internal_value(self, data):
#         try:
#             try:
#                 obj_id = data['id']
#                 return UserOrganisation.objects.get(id=obj_id)
#             except KeyError:
#                 raise serializers.ValidationError(
#                    'id is a required field.'
#                 )
#             except ValueError:
#                 raise serializers.ValidationError(
#                     'id must be an integer.'
#                 )
#         except UserOrganisation.DoesNotExist:
#             raise serializers.ValidationError(
#             'Obj does not exist.'
#             )
# class RelatedFieldAlternative(serializers.PrimaryKeyRelatedField):
#     def __init__(self, **kwargs):
#         self.serializer = kwargs.pop('serializer', None)
#         if self.serializer is not None and not issubclass(self.serializer, serializers.Serializer):
#             raise TypeError('"serializer" is not a valid serializer class')

#         super().__init__(**kwargs)

#     def use_pk_only_optimization(self):
#         return False if self.serializer else True

#     def to_representation(self, instance):
#         if self.serializer:
#             return self.serializer(instance, context=self.context).data
#         return super().to_representation(instance)


class SurveyResponseSerializer(serializers.ModelSerializer):
    question_responses = QuestionResponseSerializer(many=True, required=False)
    #user_organisation = RelatedFieldAlternative(queryset=UserOrganisation.objects.all(), serializer=UserOrganisationSerializer)
    user_organisation = UserOrganisationSerializer(read_only=True)

    class Meta:
        model = SurveyResponse
        fields = '__all__'
        # read_only_fields = ['survey', 'user_organisation', 'token']
    
    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['user_organisation'] = UserOrganisationSerializer(instance.user_organisation).data
    #     return response

    # def create(self, validated_data):
    #     print(validated_data)
    #     token = "".join(random.choice(string.ascii_letters) for i in range(8))
    #     user_organisation = validated_data.pop('user_organisation')
    #     print(validated_data)
    #     # print(user_organisation.survey_responses)
    #     direct_indicators = DirectIndicator.objects.filter(surveys=validated_data.get('survey'))
    #     survey_response = SurveyResponse.objects.create(**validated_data, token=token)

    #     for direct_indicator in direct_indicators.values():
    #         question_response = QuestionResponse.objects.create(survey_response=survey_response, direct_indicator_id=direct_indicator['id'])
    #         question_response.save()
    #     # survey_response.save_question_responses(question_responses)
    #     return survey_response

    def update(self, survey_response, validated_data):
        # print(validated_data, 'ddddddd')
        print('check')
        survey_response.finished = validated_data.get('finished', survey_response.finished)
        question_responses = validated_data.pop('question_responses')
        question_responses_dict = dict((i.id, i) for i in survey_response.question_responses.all())
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
        survey_response.save()
        print('>>>>>>', survey_response.finished)
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

    