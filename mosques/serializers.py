from rest_framework import serializers
from .models import (
    Region,
    City,
    Mosque,
)
from lessons.serializers import (
    LessonSerializer,
)

class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = (
            'id',
            'name',
        )


class RegionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = (
            'id',
            'name',
        )


class CityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = (
            'id',
            'name',
            'region'
        )


class MosqueSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(
        many = True
    )
    class Meta:
        model = Mosque
        fields = (
            'id',
            'name',
            'image',
            'lessons'
        )