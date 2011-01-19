from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name

class Picture(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='pictures')
    category = models.ManyToManyField(Category)
    photographer = models.ForeignKey(User)
    location = models.CharField(max_length=100, blank=True)
    date_taken= models.DateField()
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_updated = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return self.title
