from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=250, null=False, default="unknown")
    email = models.EmailField(null=True)
    age = models.IntegerField(default=10)
    address = models.TextField(default='unknown')
    # ADD 2 MORE FIELDS ONE BOOLEAN AND ONE FLOAT