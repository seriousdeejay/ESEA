from rest_framework.response import Response 
from rest_framework import viewsets, response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.renderers import JSONRenderer
from django.shortcuts import get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import yaml

from ..models import Method, Organisation, CustomUser, Topic, DirectIndicator, Survey
from ..serializers import MethodSerializer


class MethodViewSet(viewsets.ModelViewSet):
    serializer_class = MethodSerializer

    def get_queryset(self):
        network = self.request.GET.get('network', None)
        organisation = self.request.GET.get('organisation', None)
        excludenetwork = self.request.GET.get('excludenetwork', None)
        if network is not None:
            return Method.objects.filter(networks=network)
        if organisation is not None:
            return Method.objects.filter(organisations=organisation).distinct()
        if excludenetwork is not None:
            return Method.objects.exclude(networks=excludenetwork)
        return Method.objects.filter(Q(created_by=self.request.user) | Q(ispublic = True))

    def create(self, serializer):
        serializer = MethodSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=self.request.user)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        method_object = get_object_or_404(Method, pk=self.get_object().id)
        for instance in request.data:
            try:
                organisation = get_object_or_404(Organisation, id=instance['id'])
                if method_object.organisations.filter(id=organisation.id).exists():
                    method_object.organisations.remove(organisation)
                else:
                    method_object.organisations.add(organisation)
            except:
                return Response({"Error"})
        serializer = MethodSerializer(method_object)
        return Response(serializer.data)
        

@method_decorator(csrf_exempt, name='dispatch')
@api_view(['GET', 'POST'])
@permission_classes((AllowAny, ))
def upload_yaml(request):
    # if request.method == 'POST':
    #     print('>', request.FILES)
    #     print(request.data)
    #     return Response({"message": "data received!", "data": ""})
    if request.method == 'POST' and request.FILES['file']:
        myfile = request.FILES['file']
        ##Try/Except to catch YAML related errors
        try:
            YAML_dict = yaml.safe_load(myfile)
            currentuser = CustomUser.objects.get(id=1)
            m = Method.objects.create(name="BIA", description="A Method description", created_by=currentuser)
            print(m)
            topic_dict = {}
            ##Saving Topics
            for topic_key in YAML_dict['topics']:
                topic=YAML_dict['topics'][topic_key]
                description = None
                name=topic['name']
                if 'description' in topic.keys():
                    description = topic['description']
                if not 'topic' in topic.keys():
                    supertopic = Topic.objects.create(name=name, description=description, parent_topic=None, method=m)
                    topic_dict[topic_key] = supertopic
                    ## print(topic_key, supertopic)
                else:            
                    subtopic = Topic.objects.create(name=name, description=description, parent_topic=topic_dict[topic['topic']], method=m)
                    topic_dict[topic_key] = subtopic
                    print(topic_key, subtopic)
            ##Saving Surveys
            for survey in YAML_dict['surveys']:
                YAML_dict['surveys'][survey]
                descriptiom, welcomeText, closingText = None, None, None
                name = YAML_dict['surveys'][survey]['name']
                responserate = YAML_dict['surveys'][survey]['responserate']
                if 'description' in YAML_dict['surveys'][survey].keys():
                    description = YAML_dict['surveys'][survey]['description']
                if 'welcometext' in YAML_dict['surveys'][survey].keys():
                    welcomeText = YAML_dict['surveys'][survey]['welcometext']
                if 'closingtext' in YAML_dict['surveys'][survey].keys():
                    closingText = YAML_dict['surveys'][survey]['closingtext']
                s = Survey.objects.create(name=name, description=description, anonymous=False, method=m)
                ## print(s)
                ##Saving Questions
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
                        if question['answertype'] == "RADIO":
                            options = question['options']
                        if question['answertype'] == "multipleChoice":
                            answertype = "CHECKBOX"
                            options = question['aggregatedqs']
                        q = DirectIndicator.objects.create(key=key, topic=topic, answertype=answertype, name=name, isMandatory=isMandatory, description=description, instruction=instruction, options=options)
                        s.questions.add(q)
                        ## print('>>', q, 'TOPIC:', q.topic, q.question.options.all())
                    except:
                        continue
            return Response({"Method Saved!"})
        except yaml.YAMLError as exc:
            print(exc)
            return Response({exc})
    return Response({"Nothing uploaded"})
