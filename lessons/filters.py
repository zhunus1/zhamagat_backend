import django_filters as filters
from .models import (
    Lesson,
)
from mosques.models import (
    City,
)

class LessonFilter(filters.FilterSet):
    city = filters.ModelChoiceFilter(
        field_name = "mosque__city",
        queryset = City.objects.all()
    )
    class Meta:
        model = Lesson
        fields = (
            'city',
            'mosque',
            'type',
            'periodicity',
            'teacher',
            'gender',
            'start_time',
            'end_time',
        )