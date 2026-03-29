"""
URL configuration for portfolio app.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactMessageViewSet, ProjectViewSet, SkillViewSet

router = DefaultRouter()
router.register(r'contacts', ContactMessageViewSet, basename='contact')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'skills', SkillViewSet, basename='skill')

urlpatterns = [
    path('', include(router.urls)),
]
