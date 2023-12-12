
from django.db import models
from .group import Group

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name=models.CharField(max_length=100)
    # email=models.EmailField()
    # password=models.CharField(max_length=20)
    branch=models.CharField(max_length=30, blank=True, null=True)
    year=models.IntegerField(null=True,blank=True)
    userTag=models.CharField(max_length=100, blank=True, null=True)
    group=models.ManyToManyField(Group, blank=True, null=True)
    profile_pic = models.URLField(max_length=500, blank=True, null=True)
    enrollmentNo = models.IntegerField(unique=True,null=True)
    # access_token = models.CharField(max_length=255, blank=True, null=True)
    # refresh_token = models.CharField(max_length=255, blank=True, null=True)
    
    REQUIRED_FIELDS = ['email', 'name', 'enrollmentNo']
    
    def __str__(self):
        return self.username


 