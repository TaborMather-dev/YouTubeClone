from django.db import models

# Create your models here.


class Comment(models.Model):
    userComment = models.CharField(max_length=300)
    like = models.IntegerField()
    dislikes = models.IntegerField()
    userRelpy = models.CharField(max_length=300)
