from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
import datetime

class UsersManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):           
            errors['email'] = "Invalid email address!"
        if len(postData['email']) < 1:
            errors["email"] = "Your email cannot be blank."
        elif Users.objects.filter(email=postData['email']):
            errors['email'] = 'Email must be unique'
        if len(postData['first_name']) < 2:
            errors["first_name"] = "Your first name must be at least 2 characters long."
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Your last name must be at least 2 characters long."
        if len(postData['password']) < 8:
            errors["password"] = "Your password must be at least 8 characters long."
        if postData['password'] != postData['confirm_password']:
            errors["match"] = "Your passwords must match."
        if not (postData['first_name'].isalpha() and postData['last_name'].isalpha()):
            errors["alpha"] = "First and last name cannot contain any numbers."
        return errors
    
    def log_validator(self, postData):
        errors = {}
        if len(postData['email']) < 1:
            errors['email'] = "Your email cannot be blank."
            return errors
        elif len(Users.objects.filter(email=postData['email'])) == 0:
            errors['login'] = 'Invalid email or password.'
            return errors
        if len(postData['password']) < 8:
            errors['password'] = "Your password must be at least 8 characters long."
            return errors
        elif not bcrypt.checkpw(postData['password'].encode(), Users.objects.get(email=postData['email']).password.encode()):
            errors['login'] = 'Invalid email or password'
        return errors

class AppointmentManager(models.Manager):
    def schedule_visit_validator(self, postData):
        errors = {}
        if datetime.datetime.now() >= datetime.datetime.strptime(postData['appt'], "%Y-%m-%dT%H:%M"):
            errors['date'] = "Not a valid date."
        return errors
    
class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UsersManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.id})"

class Pets(models.Model):
    status = models.BooleanField()
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    animal = models.CharField(max_length=255)
    size = models.IntegerField()
    energy = models.IntegerField()
    friendly = models.IntegerField()
    desc = models.TextField()
    photo = models.ImageField(upload_to='images/')
    users_who_like = models.ManyToManyField(Users, related_name="liked_animals")
    
    def __str__(self):
        return f"{self.name} ({self.id})"

class Appointment(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey(Users, related_name="appointments")
    pet = models.ForeignKey(Pets, related_name="appointments")
    objects = AppointmentManager()