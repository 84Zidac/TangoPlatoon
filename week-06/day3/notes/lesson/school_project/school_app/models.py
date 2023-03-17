from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models
from .validators import *

class Locker(models.Model):
	locker_number = models.IntegerField(unique=True)
	combination = models.CharField(max_length=10, validators=[validate_locker_combination])

	def __str__(self):
		return f"LOCKER: {self.locker_number}"

class Student(models.Model):
	first_name = models.CharField(max_length=32)
	last_name = models.CharField(max_length=32)
	birth_date = models.DateField()
	locker = models.OneToOneField(Locker, null=True, blank=True, on_delete=models.CASCADE, related_name="student")

	def __str__(self):
		return f"STUDENT: {self.first_name} {self.last_name}"

class Professor(models.Model):
	first_name = models.CharField(max_length=32)
	last_name = models.CharField(max_length=32)
	start_date = models.DateField()

	def __str__(self):
		return f"PROFESSOR: {self.first_name} {self.last_name}"

class Course(models.Model):
	name = models.CharField(max_length=64)
	description = models.TextField()
	credits = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
	professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name="course")
	students = models.ManyToManyField(Student, through="Enrollment")

	def __str__(self):
		return f"COURSE: {self.name}"

class Enrollment(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="enrollments")
	course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
	grade = models.CharField(max_length=2, validators=[RegexValidator(regex=r"[ABCDF][+-]?")])

	class Meta:
		unique_together = (("student", "course"))

	def __str__(self):
		return f"ENR: {self.student} in {self.course}"