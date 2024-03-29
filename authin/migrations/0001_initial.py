# Generated by Django 5.0.2 on 2024-03-03 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30, unique=True)),
                ('pass_word', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='user_auth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('pass_word', models.CharField(max_length=30)),
            ],
        ),
    ]
