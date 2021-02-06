from django.urls import path, include
from .views import PostView, RegisterUserView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('account/register/', RegisterUserView.as_view()),
    path('api-token/', TokenObtainPairView.as_view()),
    path('ap-refresh/', TokenRefreshView.as_view()),
    path('posts/', PostView.as_view(), name='post_view')
]