# Generated by Django 4.2.1 on 2023-06-11 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_promote_active_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='productpromote',
            name='link',
            field=models.CharField(default='#', max_length=256),
        ),
    ]