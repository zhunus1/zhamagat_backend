from rest_framework import serializers
from .models import (
    LessonTeacher,
    LessonType,
    LessonDegree,
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


class LessonDegreeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonDegree
        fields = (
            'id',
            'name',
        )


class LessonSerializer(serializers.ModelSerializer):
    type = LessonTypeDetailSerializer()
    teacher = LessonTeacherDetailSerializer()
    gender = serializers.CharField(source='get_gender_display')
    week_day = serializers.CharField(source='get_week_day_display')
    class Meta:
        model = Lesson
        fields = (
            'type',
            'degree_type',
            'gender',
            'teacher',
            'start_time',
            'end_time',
            'week_day',
            'start_date'
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