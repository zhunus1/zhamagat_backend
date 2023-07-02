import django_filters as filters
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from .serializers import (
    MosqueSerializer,
    CityListSerializer
)
from .models import (
    Mosque,
    City
)
from .filters import (
    MosqueFilter,
)

# Create your views here.
class CityViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CityListSerializer
    queryset = City.objects.all()


class MosqueViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MosqueSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MosqueFilter

    def get_queryset(self):
        queryset = Mosque.objects \
            .select_related(
                'city',
            ).prefetch_related(
                'lessons',
            ).all()
        return queryset
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['gender'] = self.request.query_params.get('gender')
        return context
    
    