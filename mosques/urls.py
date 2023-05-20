from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mosques import views

router = DefaultRouter()
router.register(r'', views.MosqueViewSet, basename="mosque")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]