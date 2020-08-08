from django.db import models

'''
Stores a username as a primary key for a model containing an accounts email
Allows the system to take user input for a public username and map it to a private email to access data on the database
MySQL tables do not allow for duplicate primary_keys, and it was decided to store an email as the primary key to so that a user can more easily remember their login
'''




class ProfileKey(models.Model):
    username = models.CharField(max_length=200, primary_key=True)
    email = models.EmailField(max_length=200)
    