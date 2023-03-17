from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models
from datetime import datetime, date
from .validators import *


class SwimRecord(models.Model):


    # delete me when you start writing in validations
    first_name = models.CharField(max_length=32, blank=False)
    last_name = models.CharField(max_length=32, blank=False)
    team_name = models.CharField(max_length=255, blank=False)
    relay = models.BooleanField()
    stroke = models.CharField(max_length=20, validators=[validate_stroke])
    distance = models.IntegerField( validators=[validate_distance])
    record_date = models.DateTimeField(validators=[validate_record_date])
    record_broken_date = models.DateField()

    
