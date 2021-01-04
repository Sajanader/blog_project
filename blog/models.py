from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=64)
    auther = models.ForeignKey('auth.User',on_delete = models.CASCADE)
    body = models.TextField(max_length=100)

    def __str__(self):
        return self.title