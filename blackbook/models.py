from django.db import models
from django.contrib.auth.models import User

from PIL import Image

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
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
    date_taken= models.DateField()
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_updated = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return self.title

    def save(self, size=(1000, 580)):
        if not self.id and not self.image:
            return

        super(Photo, self).save()

        filename = self.image.path
        image = Image.open(filename)

        image.thumbnail(size, Image.ANTIALIAS)
        image.save(filename)
