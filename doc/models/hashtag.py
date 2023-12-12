from django.db import models

from .document import Document


class Hashtag(models.Model):
    container = models.ForeignKey(Document, on_delete=models.CASCADE, related_name="tags")
    hashtag = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.hashtag