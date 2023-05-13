# Generated by Django 4.2.1 on 2023-05-13 10:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mosques', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mosque',
            name='image',
            field=models.FileField(upload_to='mosques/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])], verbose_name='Изображение'),
        ),
    ]
