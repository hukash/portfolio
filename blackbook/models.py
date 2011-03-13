from django.db import models
from django.contrib.auth.models import User

from PIL import Image



class Category(models.Model):
    FORMAT_CHOICES = (
        (u'landscape', u'Landscape'),
        (u'portrait', u'Portrait'),
    )    
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    format = models.CharField(max_length=10, choices=FORMAT_CHOICES)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.name

class Photo(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='photos')
    category = models.ManyToManyField(Category)
    photographer = models.ForeignKey(User)
    location = models.CharField(max_length=100, blank=True)
    active = models.BooleanField(default=True)
    date_taken = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_updated = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return self.title

    def save(self, size=(874, 585)):
        if not self.id and not self.image:
            return

        super(Photo, self).save()

        filename = self.image.path
        image = Image.open(filename)

        image.thumbnail(size, Image.ANTIALIAS)
        image.save(filename)

class Video(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    url = models.URLField(verify_exists=True)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_updated = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return self.title
