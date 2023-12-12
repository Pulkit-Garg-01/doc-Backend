from django.db import models
from .user import User

class template(models.Model):
    name=models.CharField(max_length=50)
    createdBy=models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField()