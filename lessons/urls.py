from django.urls import path, include
from rest_framework.routers import DefaultRouter
from lessons import views

router = DefaultRouter()
router.register(r'lessons', views.LessonViewSet, basename="lesson")
router.register(r'banners', views.BannerViewSet, basename="banner")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]