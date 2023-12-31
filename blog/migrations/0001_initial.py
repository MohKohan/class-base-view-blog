# Generated by Django 4.2.4 on 2023-08-31 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('is_deleted', models.BooleanField(default=False)),
                ('is_updated', models.DateTimeField(auto_now=True)),
                ('is_created', models.DateTimeField(auto_now_add=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('categoryName', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SightseeingPlaces',
            fields=[
                ('is_deleted', models.BooleanField(default=False)),
                ('is_updated', models.DateTimeField(auto_now=True)),
                ('is_created', models.DateTimeField(auto_now_add=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
