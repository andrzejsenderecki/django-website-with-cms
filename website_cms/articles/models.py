from django.db import models
from django.conf import settings

class Article(models.Model):
    title = models.CharField(max_length=180)
    content = models.TextField()
    image = models.FileField(upload_to='images/')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    published = models.DateTimeField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    content = models.TextField()
    published = models.DateTimeField()

    def __str__(self):
        return self.name


