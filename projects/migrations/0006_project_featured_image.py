# Generated by Django 5.1.2 on 2024-10-25 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_review_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]