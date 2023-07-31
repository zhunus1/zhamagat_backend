import django_filters as filters
from .models import (
    Mosque,
)

from lessons.models import (
    Lesson,
)

class MosqueFilter(filters.FilterSet):
    class Meta:
        model = Mosque
        fields = (
            'city',
        )

