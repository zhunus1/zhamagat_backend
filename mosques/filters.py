import django_filters as filters
from .models import (
    Mosque,
)

class MosqueFilter(filters.FilterSet):
    class Meta:
        model = Mosque
        fields = (
            'city',
        )

