# Generated by Django 4.2 on 2023-05-01 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=255)),
            ],
        ),
    ]