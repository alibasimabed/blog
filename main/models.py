from django.db import models


class Post(models.Model):
    upload = models.ImageField(upload_to ='uploads/')
    title = models.CharField(max_length=200, unique=True)
    desci = models.CharField(max_length=300, default= '')
    tag = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
