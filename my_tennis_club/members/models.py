from django.db import models
from django.utils import timezone

class User(models.Model):
    USER_ROLES = [
        ('student', 'Student'),
        ('admin', 'Admin'),
    ]

    user_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    role = models.CharField(max_length=10, choices=USER_ROLES)
    created_at = models.DateTimeField(default=timezone)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Course(models.Model):
    course_id = models.AutoField(primary_key=True, default='DEFAULT_CODE')
    course_name = models.CharField(max_length=100, null=True)
    course_code = models.CharField(max_length=10, unique=True, default='DEFAULT_CODE')
    credits = models.IntegerField(default='DEFAULT_CODE')
    created_at = models.DateTimeField(default=timezone)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name


class Result(models.Model):
    result_id = models.AutoField(primary_key=True, default='DEFAULT_CODE')
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)
    score = models.DecimalField(max_digits=5, decimal_places=2, default='DEFAULT_CODE')
    grade = models.CharField(max_length=2, default='DEFAULT_CODE')
    academic_year = models.CharField(max_length=10, default='DEFAULT_CODE')
    created_at = models.DateTimeField(default=timezone)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.firstname} {self.user.lastname} - {self.course.course_name} - Score: {self.score}, Grade: {self.grade}, Year: {self.academic_year}"