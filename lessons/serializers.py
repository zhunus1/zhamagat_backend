from rest_framework import serializers
from .models import (
    LessonTeacher,
    LessonType,
    Lesson,
    Banner
)
from mosques.models import (
    City,
    Mosque
)

class LessonTeacherDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonTeacher
        fields = (
            'id',
            'name',
        )


class LessonTypeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonType
        fields = (
            'id',
            'name',
        )


class LessonSerializer(serializers.ModelSerializer):
    type = LessonTypeDetailSerializer()
    teacher = LessonTeacherDetailSerializer()
    class Meta:
        model = Lesson
        fields = (
            'type',
            'teacher',
            'start_time',
            'end_time',
            'date'
        )


class BannerSerializer(serializers.ModelSerializer):
    city_id = serializers.SerializerMethodField()
    mosque_id = serializers.SerializerMethodField()

    class Meta:
        model = Banner
        fields = (
            'id',
            'image',
            'lesson',
            'featured',
            'city_id',
            'mosque_id'
        )
    
    def get_city_id(self, obj):
        return obj.lesson.mosque.city.id

    def get_mosque_id(self, obj):
        return obj.lesson.mosque.id