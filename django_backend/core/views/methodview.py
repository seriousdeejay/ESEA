from rest_framework.response import Response 
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import yaml

from ..models import Method, CustomUser, Topic, DirectIndicator, Survey
from ..serializers import MethodSerializer


class MethodViewSet(viewsets.ModelViewSet):
    serializer_class = MethodSerializer

    def get_queryset(self):
        #if False: #self.request.user.is_authenticated:
        #    pass
            # user = self.request.user
            # return Method.objects.filter(Q(organisation that are accessible for user) | Q(ispublic = True)) ??
        # return Method.objects.filter(ispublic=True)
        network = self.request.GET.get('network', None)
        organisation = self.request.GET.get('organisation', None)
        if network is not None:
            return Method.objects.filter(organisations__network=network).distinct()
        if organisation is not None:
            return Method.objects.filter(organisations=organisation)
        return Method.objects.all()

    def create(self, serializer):
        # creator = get_object_or_404(CustomUser, pk=self.request.user.id)
        serializer = MethodSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)        

# @method_decorator(csrf_exempt, name='dispatch')
@api_view(['GET', 'POST'])
def upload_yaml(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        ### Try/Except to catch YAML related errors
        try:
            YAML_dict = yaml.safe_load(myfile)
            m = Method.objects.create(name="BIA", description="A Method description")
            print(m)
            topic_dict = {}
            ### Saving Topics
            for topic_key in YAML_dict['topics']:
                topic=YAML_dict['topics'][topic_key]
                description = None
                name=topic['name']
                if 'description' in topic.keys():
                    description = topic['description']
                if not 'topic' in topic.keys():
                    supertopic = Topic.objects.create(name=name, description=description, parent_topic=None, method=m)
                    topic_dict[topic_key] = supertopic
                    print(topic_key, supertopic)
                else:            
                    subtopic = Topic.objects.create(name=name, description=description, parent_topic=topic_dict[topic['topic']], method=m)
                    topic_dict[topic_key] = subtopic
                    print(topic_key, subtopic)
            ### Saving Surveys
            for survey in YAML_dict['surveys']:
                YAML_dict['surveys'][survey]
                descriptiom, welcomeText, closingText = None, None, None
                name = YAML_dict['surveys'][survey]['name']
                responserate = YAML_dict['surveys'][survey]['responserate']
                if 'description' in YAML_dict['surveys'][survey].keys():
                    description = YAML_dict['surveys'][survey]['description']
                # if 'welcometext' in YAML_dict['surveys'][survey].keys():
                #     welcomeText = YAML_dict['surveys'][survey]['welcometext']
                # if 'closingtext' in YAML_dict['surveys'][survey].keys():
                #     closingText = YAML_dict['surveys'][survey]['closingtext']
                s = Survey.objects.create(name=name, description=description, anonymous=False, stakeholder=None, method=m)
                print(s)
                ### Saving Questions
                for question in YAML_dict['surveys'][survey]['questions']:
                    question = YAML_dict['surveys'][survey]['questions'][question]
                    isMandatory, description, instruction, options = True, None, None, None
                    try:
                        key = question['indicator']
                        topic = topic_dict[question['topic']]
                        answertype = question['answertype']
                        name = question['name']
                        if question['ismandatory'] == "N":
                            isMandatory = False
                        if 'description' in question.keys():
                            description = question['description']
                        if 'options' in question.keys(): 
                            options = question['options']
                        q = DirectIndicator.objects.create(key=key, topic=topic, answertype=answertype, name=name, isMandatory=isMandatory, description=description, instruction=instruction, options=options)
                        print('>>', q, 'TOPIC:', q.topic, q.question.options.all())
                    except:
                        continue
                return Response({"Method Saved!"})
        except yaml.YAMLError as exc:
            print(exc)
            return Response({exc})
    return Response({"Nothing uploaded"})
