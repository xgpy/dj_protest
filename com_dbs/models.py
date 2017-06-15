from django.db import models
from django.template.defaultfilters import default
import datetime,django.utils

# Create your models here.

class python_stru(models.Model):
    title_level=models.IntegerField()
    maintitle=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    
class python_title(models.Model):
    title=models.CharField(max_length=100)
    t_level=models.IntegerField()
    pre_title=models.CharField(max_length=100)
    note_date=models.DateTimeField(auto_now_add=True)
    visit_count=models.IntegerField(default=0)
    
class python_cont(models.Model):
#     cont_title=models.ForeignKey('python_title')
    cont_title=models.CharField(max_length=100)
    cont_py=models.TextField()

class blogs_chat(models.Model):
    username=models.CharField(max_length=50)
    chat_cont=models.CharField(max_length=500)
    chat_date=models.DateTimeField(auto_now=True)
    
class comment_python(models.Model):
    comment_user=models.CharField(max_length=50)
    comment_cont=models.CharField(max_length=500)
    comment_date=models.DateTimeField(auto_now=True)
    prereply_date=models.DateTimeField(default=django.utils.timezone.now)
    comment_title=models.ForeignKey('python_title')
    comment_reply=models.CharField(max_length=50,default='0')
    comment_level=models.IntegerField()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    