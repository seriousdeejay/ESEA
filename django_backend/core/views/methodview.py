from rest_framework.response import Response 
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import yaml

from ..models import Method, CustomUser

from ..models import Method
from ..serializers import MethodSerializer

class MethodViewSet(viewsets.ModelViewSet):
    serializer_class = MethodSerializer

    def get_queryset(self):
        #if False: #self.request.user.is_authenticated:
        #    pass
            # user = self.request.user
            # return Method.objects.filter(Q(organisation that are accessible for user) | Q(ispublic = True)) ??
            # return Organisation.objects.filter(Q(creator=user) | Q(ispublic = True))
        return Method.objects.all()

    def create(self, serializer):
        # creator = get_object_or_404(CustomUser, pk=self.request.user.id)
        # print(creator)
        serializer = MethodSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)        

@method_decorator(csrf_exempt, name='dispatch')
def upload_yaml(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        # print(myfile.read())
        try:
            yamldict = yaml.safe_load(myfile)
            print(yamldict['topics']['C1'])
            for key in yamldict['topics']:
                print(key, {'name': yamldict['topics'][key]['name']})
                # try:
                #     # print({'description': dict['topics'][key]['description']})
                # except:
                #     # print('No Description Found')
        except yaml.YAMLError as exc:
            print(exc)