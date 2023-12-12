from django.db import models
from .user import User
from .document import Document


class Permission(models.Model):
    permission_choices = [
        ('R', "Read only"),
        ('RW', "Read and Write")
    ]
    
    userId=models.ForeignKey(User, on_delete=models.CASCADE)
    docId=models.ForeignKey(Document,on_delete=models.CASCADE)
    permission=models.CharField(max_length=2,choices=permission_choices)
    
    def __str__(self):
        return self.permission