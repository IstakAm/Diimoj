# Generated by Django 4.2.1 on 2023-06-09 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_promote'),
    ]

    operations = [
        migrations.AddField(
            model_name='promote',
            name='category',
            field=models.CharField(choices=[('st', 'start'), ('se', 'services')], default='st', max_length=64),
        ),
    ]
