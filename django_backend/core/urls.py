from django.urls import path, include
from .views import postview, userview
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)


urlpatterns = [
    path('account/register/', userview.RegisterUserView.as_view(), name='user_registration'),
    path('api-token/', TokenObtainPairView.as_view()),
    path('ap-refresh/', TokenRefreshView.as_view()),
    path('posts/', postview.PostView.as_view(), name='post_view')
]