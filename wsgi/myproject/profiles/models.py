from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class Profiles(models.Model):
    idnum = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    school = models.CharField(max_length=200)
    course = models.CharField(max_length=50)
    year = models.CharField(max_length = 20)
    

def __unicode__(self):
    return self.name

def get_absolute_url(self):
    return reverse('profiles_edit',kwargs={'pk':self.pk})

