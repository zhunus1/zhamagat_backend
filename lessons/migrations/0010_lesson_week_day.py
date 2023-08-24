# Generated by Django 4.2.1 on 2023-08-24 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0009_lessondegree_lesson_start_date_alter_lesson_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='week_day',
            field=models.CharField(choices=[('MN', 'Понедельник'), ('TU', 'Вторник'), ('WD', 'Среда'), ('TH', 'Четверг'), ('FR', 'Пятница'), ('ST', 'Суббота'), ('SN', 'Воскресенье')], default=1, max_length=7, verbose_name='День недели'),
            preserve_default=False,
        ),
    ]
