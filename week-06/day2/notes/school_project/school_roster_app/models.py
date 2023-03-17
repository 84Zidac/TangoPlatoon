from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=250, null=False, default='unknown')
    email = models.EmailField(null=True, default='none')
    age = models.IntegerField(default=0)