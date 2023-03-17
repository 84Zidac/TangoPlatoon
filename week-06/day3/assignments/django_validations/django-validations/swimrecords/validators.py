import re
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
import pytz

def validate_stroke(stroke):
    strokes = ['front crawl', 'butterfly', 'breast', 'back', 'freestyle']
    if stroke not in strokes:
        raise ValidationError(f'{stroke} is not a valid stroke')
    
def validate_distance(distance):
    if distance < 50:
        raise ValidationError('Ensure this value is greater than or equal to 50.')
    
def validate_record_date(record_date):
    time_now = datetime.now(pytz.utc)
    if record_date > time_now:
        raise ValidationError("Can't set record in the future.")
    
def validate_record_broken_date(record_broken_date):
    if record_broken_date < record_date:
        raise ValidationError("Can't break record before record was set.")