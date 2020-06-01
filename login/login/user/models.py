from django.db import models
from django.contrib.auth.models import AbstractUser


class Post(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.title

class User(AbstractUser):
    age=models.IntegerField(default=0)
    sex_choice=((0,'nữ'),(1,'nam'))
    sex=models.IntegerField(choices=sex_choice,default=0)
