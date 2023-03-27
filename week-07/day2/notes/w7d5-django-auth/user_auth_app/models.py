from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class App_User(AbstractUser):
    email = models.EmailField(blank = False, null = False, unique = True)
    name = models.CharField(max_length = 255, null = False, blank = False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return f"{self.name} | {self.email}"
    
class Task(models.Model):
    title = models.CharField(blank=False, null=False, max_length=255)
    description = models.TextField()
    user = models.ForeignKey(App_User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} | {self.user}"