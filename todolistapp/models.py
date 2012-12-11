from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    STATE_CHOICES = (
        (u'P', u'Pending'),
        (u'X', u'Cancelled'),
        (u'C', u'Completed'),
    )
    state = models.CharField(max_length=1, choices=STATE_CHOICES, default=u'P')
    creation_date = models.DateTimeField(auto_now_add=True)
    limit_date = models.DateTimeField(null=False, blank=False)
    completed_date = models.DateTimeField(blank=True)
    category = models.ForeignKey(Category)
    owner = models.ForeignKey(User)

    class Meta:
        verbose_name_plural = 'Tasks'

    def __unicode__(self):
        return self.title
