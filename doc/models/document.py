from django.db import models
from .user import User 
from ckeditor.fields import RichTextField
    

class Document(models.Model):
    Title=models.CharField(max_length=50)
    content=RichTextField()
    # hashtags=models.TextField(default='')
    createdBy=models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    created=models.DateTimeField()
    lastEditBy=models.ForeignKey(User, on_delete=models.CASCADE, related_name="lastEditBy")
    lastModified=models.DateTimeField()
    deadline=models.DateTimeField(null=True)
    
    def __str__(self):
        return f"{self.Title} {self.created}"