from django.db import models

# Create your models here.
'''
Models in Django is a way to interact with database
'''

class TodoItem(models.Model):
    content = models.TextField()


