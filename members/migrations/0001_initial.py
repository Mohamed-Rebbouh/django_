# Generated by Django 5.0.2 on 2024-02-14 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('famname', models.TextField()),
                ('cardnum', models.TextField()),
                ('year', models.TextField()),
                ('birth', models.DateField()),
            ],
        ),
    ]
