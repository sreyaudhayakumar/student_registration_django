# Generated by Django 4.2.3 on 2023-11-23 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('place', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('photo', models.FileField(upload_to='')),
            ],
        ),
    ]
