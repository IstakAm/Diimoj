from datetime import datetime

from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128)


class Project(models.Model):
    title = models.CharField(max_length=256)
    description = RichTextField()
    cover = models.FileField(upload_to='files/covers/')
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    promote = models.BooleanField(default=False)


class ProjectCategory(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='category')
    category = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='projects')


class ProjectFile(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='files')
    file = models.FileField('files/projects_files/')


class Promote(models.Model):
    title = models.CharField(max_length=32, blank=False, null=False)
    description = models.CharField(max_length=256, blank=False, null=False)
    cover = models.FileField(upload_to='files/promote_covers/')
    category = models.CharField(max_length=64, choices=[('st', 'start'), ('pr', 'project')], default='st')
    link = models.CharField(max_length=256, blank=True)
    active_index = models.IntegerField(default=0, null=False, blank=False)


class Icon(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False, default='icon')
    link = models.CharField(max_length=256, blank=False, null=False)

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=32, blank=False, null=False)
    description = models.CharField(max_length=256, blank=False, null=False)
    icon_class = models.CharField(max_length=256, blank=False, null=False)
    link = models.CharField(max_length=256, blank=False, null=False)
    active_index = models.IntegerField(default=0, null=False, blank=False)


class ProductPromote(models.Model):
    cover = models.FileField(upload_to='files/promote_covers/')
    title = models.CharField(max_length=32, blank=False, null=False)
    description = models.CharField(max_length=256, blank=False, null=False)
    link = models.CharField(max_length=256, blank=False, null=False, default='#')
    active_index = models.IntegerField(default=0, null=False, blank=False)


