# Generated by Django 4.1 on 2022-08-27 14:31

import apps.about_us.models.about_us
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('image1', models.ImageField(upload_to=apps.about_us.models.about_us.upload_location)),
                ('image2', models.ImageField(upload_to=apps.about_us.models.about_us.upload_location)),
                ('fact1', models.TextField(blank=True, null=True)),
                ('fact2', models.TextField(blank=True, null=True)),
            ],
        ),
    ]