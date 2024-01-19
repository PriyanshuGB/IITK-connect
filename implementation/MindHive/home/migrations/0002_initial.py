# Generated by Django 3.2.12 on 2022-03-14 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='content',
            name='dislikedBy',
            field=models.ManyToManyField(blank=True, related_name='dislikedBy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='content',
            name='likedBy',
            field=models.ManyToManyField(blank=True, related_name='likedBy', to=settings.AUTH_USER_MODEL),
        ),
    ]
