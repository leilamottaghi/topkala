# Generated by Django 4.2.5 on 2023-09-16 10:53

from django.db import migrations, models
import topkalaTemplate.models


class Migration(migrations.Migration):

    dependencies = [
        ('topkalaTemplate', '0004_sliderimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderimage',
            name='image',
            field=models.ImageField(upload_to=topkalaTemplate.models.slider_image_path),
        ),
    ]