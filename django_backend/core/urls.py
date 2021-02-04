from django.urls import path, include
from .views import PostView

urlpatterns = [
    path('posts/', PostView.as_view(), name='post_view')
]