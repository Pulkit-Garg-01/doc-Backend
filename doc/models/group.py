from django.db import models

class Group(models.Model):
    name=models.CharField( max_length=100)
    tag=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name