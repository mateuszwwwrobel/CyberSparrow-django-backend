# Generated by Django 3.0.7 on 2021-03-23 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('start_date', models.CharField(max_length=8)),
                ('finish_date', models.CharField(max_length=8)),
                ('final_project', models.CharField(max_length=300)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('start_date', models.CharField(max_length=8)),
                ('finish_date', models.CharField(max_length=8)),
                ('description', models.TextField()),
            ],
        ),
    ]
