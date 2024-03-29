import django_filters as filters
from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    LessonType,
    LessonDegree,
    Lesson,
    Banner
)
from .serializers import (
    LessonTypeDetailSerializer,
    LessonDegreeDetailSerializer,
    LessonSerializer,
    BannerSerializer,
)
from .filters import (
    LessonFilter,
)

# Create your views here.
class LessonTypeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LessonTypeDetailSerializer
    queryset = LessonType.objects.all()


class LessonDegreeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LessonDegreeDetailSerializer
    queryset = LessonDegree.objects.all()


class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LessonSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = LessonFilter

    def get_queryset(self):
        queryset = Lesson.objects.select_related(
            'mosque',
            'mosque__city',
            'type',
            'teacher'
        ).order_by('week_day').all()
        return queryset


class BannerViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = (
        'featured',
    )
    
