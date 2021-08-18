from django.db import models

# Create your models here.


class Comments(models.Model):
    userComment = models.CharField(max_length=300)
    like = models.IntegerField()
