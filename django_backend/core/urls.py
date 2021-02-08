from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from .views import userview, organisationview, networkview


router = DefaultRouter()
router.register(r'organisations', organisationview.OrganisationViewSet)
router.register(r'personalorganisations', organisationview.PersonalOrganisationViewSet, basename='Organisation')
router.register(r'networks', networkview.NetworkViewSet)

urlpatterns = [
    path('account/register/', userview.RegisterUserView.as_view(), name='user_registration'),
    path('api-token/', TokenObtainPairView.as_view()),
    path('ap-refresh/', TokenRefreshView.as_view()),
    path('', include(router.urls)),
    #path('organisati/', organisationview.OrganisationView.as_view(), name='organisation_view'),
    #path('organisations/<int:pk>/', organisationview.OrganisationView.as_view())
]