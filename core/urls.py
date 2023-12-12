# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CandidateViewSet, RecruiterViewSet, JobViewSet, ApplicationViewSet, MessageViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'candidates', CandidateViewSet)
router.register(r'recruiters', RecruiterViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'applications', ApplicationViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
