from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

from ..serializers import RegisterUserSerializer, UserSerializer, UserOrganisationSerializer
from ..models import CustomUser, Organisation, UserOrganisation, StakeholderGroup

import os
import csv
import string
import random


class RegisterUserView(CreateAPIView):
    serializer_class = RegisterUserSerializer

class UsersViewSet(viewsets.ReadOnlyModelViewSet):
    model = CustomUser
    serializer_class = UserSerializer

    def get_queryset(self):
        currentuser = self.request.GET.get('currentuser', None)
        network = self.request.GET.get('network', None)
        organisation = self.request.GET.get('organisation', None)
        excludeorganisation = self.request.GET.get('excludeorganisation', None)
        if currentuser is not None:
            return CustomUser.objects.filter(id=self.request.user.id)
        if network is not None:
            return CustomUser.objects.filter(organisations__networks=network).distinct() # Should pass network id(s) in order to serve the participants of network(s)
        if organisation is not None:
            return CustomUser.objects.filter(organisations=organisation)
        if excludeorganisation is not None:
            return CustomUser.objects.exclude(organisations=excludeorganisation)
        return CustomUser.objects.all()

@method_decorator(csrf_exempt, name='dispatch')
@api_view(['GET', 'POST'])
@permission_classes((AllowAny, ))
def import_employees(request, organisation_pk):
    if request.method == 'POST' and 'file' in request.FILES.keys():
        myfile = request.FILES['file']
        print(myfile)
    organisation = get_object_or_404(Organisation, pk=organisation_pk)
    cwd = os.getcwd()
    output = []
    with open(os.path.join(cwd, "core\\uploadedfiles\\uploadedemployees.csv")) as file:
        newemployees = csv.reader(file, delimiter=",", quotechar="|")
        for i, row in enumerate(newemployees):
            if (i == 0):
                pass
            else:
                try:
                    email = row[1]
                    firstname = row[2]
                    lastnameprefix =row[3]
                    lastname = row[4]
                    # username = f"{firstname.lower()}{lastnameprefix.lower()}{lastname.lower()}"
                    username = f"{firstname}{lastnameprefix}{lastname}".lower()
                    password = "".join(random.choice(string.ascii_letters) for i in range(8))
                    data = { "email": email, "first_name": firstname, "last_name_prefix": lastnameprefix, "last_name": lastname, "username": username, "password": password, "password2": password, "uniquetoken": password}
                    serializer = RegisterUserSerializer(data=data)
                    serializer.is_valid(raise_exception=True)
                    print('d')
                    serializer.save()
                    newuser = get_object_or_404(CustomUser, username=serializer.data['username'])
                    print(newuser)
                    userorganisation = UserOrganisation.objects.create(user=newuser, organisation=organisation)
                    stakeholdergroup = StakeholderGroup.objects.get(name="Employee")
                    userorganisation.stakeholdergroups.add(stakeholdergroup)
                    userorganisation.save()
                    serializer = UserSerializer(newuser)
                    output.append(serializer.data)      
                    
                except:
                    print(f"error in row {i}")

    return Response(output)
                