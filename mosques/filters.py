import django_filters as filters
from .models import (
    Mosque,
)

from lessons.models import (
    Lesson,
)

class MosqueFilter(filters.FilterSet):
    gender = filters.ChoiceFilter(
        field_name = 'lessons__gender',
        choices = Lesson.CHOICES,
    )

    class Meta:
        model = Mosque
        fields = (
            'city',
            'gender',
        )

