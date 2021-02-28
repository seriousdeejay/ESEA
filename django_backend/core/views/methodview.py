from rest_framework.response import Response 
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import yaml

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
        # print(yaml.load(myfile, Loader=yaml.FullLoader))

# def handle_uploaded_file(f):
#     with open('some/file/name.txt', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

        # File file = myfile
        # return Response.ok(file, MediaType.APPLICATION_OCTET_STREAM)
        # .header("Content-Disposition", "attachment; filename=\"" + file.getName() + "\"" ) //optional
        # .build()
        # return Response({stringg})
        # with open('myfile', 'r') as stream:
        #     try:
        #         print(yaml.safe_load(stream))
        #     except yaml.YAMLError as exc:
        #         print(exc)
        # print('Not working!')
        # fs = FileSystemStorage()
        # filename = fs.save(myfile.name, myfile)
        # uploaded_file_url = fs.url(filename)
        # return render(request, '')