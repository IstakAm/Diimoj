# Generated by Django 4.2.1 on 2023-06-10 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_icon_services_promote_link_alter_promote_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.FileField(upload_to='files/promote_covers/')),
                ('title', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=256)),
            ],
        ),
    ]
