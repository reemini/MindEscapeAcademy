from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    userEmail = models.EmailField(primary_key=True, unique=True)
    profile_pic = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=20, choices=[('educator', 'Educator'), ('admin', 'Admin'), ('student', 'Student')])

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

class AreaOfInterest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class AreaOfSpecialization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(User):
    stdID = models.AutoField(primary_key=True)
    areas_of_interest = models.ManyToManyField(AreaOfInterest)
    areas_of_specialization = models.ManyToManyField(AreaOfSpecialization)

class Educator(User):
    educatorID = models.AutoField(primary_key=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    professional_title = models.CharField(max_length=100, null=True, blank=True)
    linkedin_account = models.URLField(null=True, blank=True)
    is_official_reviewer = models.BooleanField(default=False)
    areas_of_specialization = models.ManyToManyField(AreaOfSpecialization)

class Admin(User):
    adminID = models.AutoField(primary_key=True)

