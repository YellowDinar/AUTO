# -*- coding: utf-8 -*-
from django.db import models
from django.core.files.storage import FileSystemStorage
quest_fss = FileSystemStorage(location='/media/images')

class Topic(models.Model):
    name = models.CharField('Name', max_length=200)
    about = models.TextField('Description')

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'

    def __unicode__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('Title', max_length=300)
    text = models.TextField('Description')
    image = models.ImageField('Image', blank=True, upload_to=quest_fss)
    topic = models.ForeignKey(Topic)

    class Meta:
        verbose_name = u'Post'
        verbose_name_plural = u'Posts'

    def __unicode__(self):
        return self.title