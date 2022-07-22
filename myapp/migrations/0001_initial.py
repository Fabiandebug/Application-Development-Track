# Generated by Django 4.0.6 on 2022-07-22 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='apirates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.TextField()),
                ('url', models.TextField()),
                ('count', models.IntegerField(default=0)),
                ('lastupdated', models.DateTimeField(auto_now_add=True)),
                ('maxrate', models.IntegerField(default=10)),
            ],
        ),
    ]
