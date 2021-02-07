from django.urls import path, include
from .views import userview, organisationview
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)


urlpatterns = [
    path('account/register/', userview.RegisterUserView.as_view(), name='user_registration'),
    path('api-token/', TokenObtainPairView.as_view()),
    path('ap-refresh/', TokenRefreshView.as_view()),
    path('organisations/', organisationview.OrganisationView.as_view(), name='organisation_view'),
    path('organisations/<int:pk>/', organisationview.OrganisationView.as_view())
]