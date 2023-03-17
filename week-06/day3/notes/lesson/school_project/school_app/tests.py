from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Locker # import User model

# Create your tests here.
class school_tests(TestCase):

    def test_01_create_locker_incorrect(self):
        new_locker = Locker(locker_number='102', combination='12-433')

        try:
            new_locker.full_clean()
            self.fail()

        except ValidationError as e:
            self.assertFalse('Invalid combination format!!!' in e.message_dict['combination'])