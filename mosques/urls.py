from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mosques import views

router = DefaultRouter()
router.register(r'mosques', views.MosqueViewSet, basename="mosque")
router.register(r'cities', views.CityViewSet, basename="city")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]