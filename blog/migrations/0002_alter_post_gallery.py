# Generated by Django 4.2.2 on 2023-08-01 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='gallery',
            field=models.ManyToManyField(blank=True, related_name='posts', to='blog.image', verbose_name='Galereya'),
        ),
    ]
