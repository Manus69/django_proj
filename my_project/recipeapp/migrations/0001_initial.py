# Generated by Django 5.1.7 on 2025-05-25 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('desc', models.TextField(blank=True)),
                ('alg', models.TextField(blank=True)),
                ('time', models.IntegerField()),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
    ]
