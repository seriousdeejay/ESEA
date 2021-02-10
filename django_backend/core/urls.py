from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from .views import userview, organisationview, networkview


router = DefaultRouter()
router.register(r'organisations', organisationview.OrganisationViewSet, basename='Organisations')
# router.register(r'personalorganisations', organisationview.PersonalOrganisationViewSet, basename='Organisation')
router.register(r'networks', networkview.NetworkViewSet, basename="Networks")
router.register(r'users', userview.UsersViewSet)

urlpatterns = [
    path('account/register/', userview.RegisterUserView.as_view(), name='user_registration'),
    path('api-token/', TokenObtainPairView.as_view()),
    path('ap-refresh/', TokenRefreshView.as_view()),
    path('', include(router.urls)),
    path('organisationparticipants/<int:pk>/', organisationview.OrganisationParticipantsViewSet.as_view({'get': 'list'})),
    path('networkorganisations/<int:pk>/', networkview.NetworkOrganisationsViewSet.as_view({'get': 'list'}))
]