from django.urls import path, include, re_path
from rest_framework_nested import routers
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from .views import (userview, networkview, organisationview, methodview, surveyview, topicview, direct_indicatorview, survey_responseview)


router = routers.DefaultRouter()
router.register(r'users', userview.UsersViewSet, basename="Users")
router.register(r'networks', networkview.NetworkViewSet, basename="Networks")
router.register(r'organisations', organisationview.OrganisationViewSet, basename="Organisations")
router.register(r'methods', methodview.MethodViewSet, basename='methods')   ## /methods/ & /methods/{pk}/

method_router = routers.NestedSimpleRouter(router, r'methods', lookup="method")
method_router.register(r'surveys', surveyview.SurveyViewSet, basename="method-surveys")
method_router.register(r'topics', topicview.TopicViewSet, basename="method-topics")     ## /methods/{pk}/topics & /methods/{pk}/topics/{pk}/
method_router.register(r'questions', direct_indicatorview.DirectIndicatorViewSet, basename="method-questions")

survey_router = routers.NestedSimpleRouter(method_router, r'surveys', lookup="survey")
survey_router.register(r'organisations', organisationview.OrganisationViewSet, basename="survey-organisations")

organisation_router = routers.NestedSimpleRouter(survey_router, r'organisations', lookup="organisation")
organisation_router.register(r'responses', survey_responseview.SurveyResponseViewSet, basename="organisation-responses")

# router.register(r'topics', topicview.TopicViewSet, basename='topics')
# router.register(r'questions', direct_indicatorview.DirectIndicatorViewSet, basename='questions')
# router.register(r'surveys', surveyview.SurveyViewSet, basename='surveys')
router.register(r'public-surveys', surveyview.PublicSurveyViewSet, basename='public-surveys')
# router.register(r'personalorganisations', organisationview.PersonalOrganisationViewSet, basename='Organisation')


urlpatterns = [
    path('account/register/', userview.RegisterUserView.as_view(), name='user_registration'),
    path('api-token/', TokenObtainPairView.as_view()),
    path('ap-refresh/', TokenRefreshView.as_view()),
    path('import-yaml/', methodview.upload_yaml),
    path('import-employees/<int:organisation_pk>/', userview.import_employees, name="import_employees_of_organisation"),
    path('send-surveys/', organisationview.send_surveys, name="send_surveys_to_emails"),
    path('', include(router.urls)),
    path('', include(method_router.urls)),
    path('', include(survey_router.urls)),
    path('', include(organisation_router.urls)),
]




    # path('organisationparticipants/<int:pk>/', organisationview.OrganisationParticipantsViewSet.as_view({'get': 'list'})),
    # path('networkorganisations/<int:pk>/', networkview.NetworkOrganisationsViewSet.as_view({'get': 'list'}))