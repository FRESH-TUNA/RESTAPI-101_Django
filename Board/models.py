from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50, blank=False)
    content = models.TextField(blank=True)
    publishedDate = models.DateField(auto_now_add=True)
    updatedDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
