from django.conf import settings
from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    post = models.TextField(max_length=1000)
    date_posted = models.DateTimeField(blank=True)
   
    def __str__(self):
       return self.title