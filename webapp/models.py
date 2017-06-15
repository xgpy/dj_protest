from django.db import models

# Create your models here.


class user(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.EmailField()
    user_type=models.ForeignKey('usertype')
    
class usertype(models.Model):
    name=models.CharField(max_length=50)
    