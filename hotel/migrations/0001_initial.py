# Generated by Django 5.0.2 on 2024-02-22 16:06

import django.db.models.deletion
import shortuuid.django_fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.FileField(upload_to='hotel_gallery')),
                ('address', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('disabled', 'Disabled'), ('rejected', 'Rejected'), ('in_review', 'In Review'), ('live', 'Live')], default='live', max_length=20)),
                ('tags', models.CharField(help_text='Seperate tags with commas', max_length=200)),
                ('views', models.IntegerField(default=0)),
                ('featured', models.BooleanField(default=False)),
                ('hid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxyz', length=10, max_length=20, prefix='', unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
