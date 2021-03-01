from django.urls import path, include, re_path
from rest_framework_nested import routers
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from .views import (userview, networkview, organisationview, methodview, topicview, direct_indicatorview, surveyview)


router = routers.DefaultRouter()
router.register(r'users', userview.UsersViewSet, basename="Users")
router.register(r'networks', networkview.NetworkViewSet, basename="Networks")
router.register(r'organisations', organisationview.OrganisationViewSet, basename='Organisations')
router.register(r'methods', methodview.MethodViewSet, basename='methods')   ## /methods/ & /methods/{pk}/

method_router = routers.NestedSimpleRouter(router, r'methods', lookup='method')
method_router.register(r'topics', topicview.TopicViewSet, basename="method-topics")     ## /methods/{pk}/topics & /methods/{pk}/topics/{pk}/
# router.register(r'topics', topicview.TopicViewSet, basename='topics')
router.register(r'questions', direct_indicatorview.DirectIndicatorViewSet, basename='questions')
router.register(r'surveys', surveyview.SurveyViewSet, basename='surveys')
router.register(r'public-surveys', surveyview.PublicSurveyViewSet, basename='public-surveys')
# router.register(r'personalorganisations', organisationview.PersonalOrganisationViewSet, basename='Organisation')


urlpatterns = [
    path('account/register/', userview.RegisterUserView.as_view(), name='user_registration'),
    path('api-token/', TokenObtainPairView.as_view()),
    path('ap-refresh/', TokenRefreshView.as_view()),
    path('import-yaml/', methodview.upload_yaml),
    path('', include(router.urls)),
    path('', include(method_router.urls))
    # path('organisationparticipants/<int:pk>/', organisationview.OrganisationParticipantsViewSet.as_view({'get': 'list'})),
    # path('networkorganisations/<int:pk>/', networkview.NetworkOrganisationsViewSet.as_view({'get': 'list'}))
]