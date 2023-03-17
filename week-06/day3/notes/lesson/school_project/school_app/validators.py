import re
from django.core.exceptions import ValidationError

def validate_locker_combination(combination):
    pattern = r"(^[0-9]{1,2})-([0-9]{1,2})-([0-9]{1,2}$)"
    matches = re.search(pattern, combination)
    
    if not matches:
        raise ValidationError('Invalid Combination Format')