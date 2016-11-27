from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import Permission, User

# Create your models here.

class profile(models.Model):
    user1 = models.ForeignKey(User, default=1)
    name = models.CharField(max_length = 40)
    nick_name = models.CharField(max_length = 20)
    def get_absolute_url(self):
        return reverse('webpage:profile',kwargs = { 'names' : self.nick_name})
    def __str__(self):
        return self.name


class Data(models.Model):
    user2 = models.ForeignKey(profile,on_delete = models.CASCADE)
    about= models.CharField(max_length = 200)
    email = models.EmailField()
    mobile= models.CharField(max_length = 200)
    def __str__(self):
        return self.about

class images(models.Model):
    user3 = models.ForeignKey(profile,on_delete = models.CASCADE)
    images_details = models.CharField(max_length = 200)
    images = models.CharField(max_length = 200)

class Massage(models.Model):
    user4 = models.ForeignKey(User, default=1)
    sub = models.CharField(max_length = 200)
    massage = models.CharField(max_length = 200)
