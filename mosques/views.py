import django_filters as filters
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from .serializers import (
    MosqueSerializer,
)
from .models import (
    Mosque,
)
from .filters import (
    MosqueFilter,
)

# Create your views here.

class MosqueViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MosqueSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MosqueFilter

    def get_queryset(self):
        queryset = Mosque.objects.select_related(
            'city',
        ).all()
        return queryset