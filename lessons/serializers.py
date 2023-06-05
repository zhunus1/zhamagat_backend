from rest_framework import serializers
from .models import (
    LessonTeacher,
    LessonType,
    Lesson,
    Banner
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
    class Meta:
        model = Banner
        fields = (
            'id',
            'image',
            'lesson'
        )