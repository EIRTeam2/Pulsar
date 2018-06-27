from django.conf.urls import url, include
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'milestones', views.MilestoneViewSet)
router.register(r'design_elements', views.DesignElementViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
