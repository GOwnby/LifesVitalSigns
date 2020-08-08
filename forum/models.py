from django.db import models
import datetime


# A Life's Vital Signs Forum account
class Account(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    verified = models.NullBooleanField(default=False)
    about_me = models.CharField(max_length=1000, default='I have no life!')
    profile_pic = models.ImageField(upload_to='profilepictures', default='profilepictures/default.jpg')
    level = models.IntegerField(default=1)
    level_text = models.CharField(max_length=50, default='Citizen Scientist')
    posts = models.IntegerField(default=0)
    forum_signature = models.CharField(max_length=100, default='No Signature')
    uuid = models.CharField(max_length=500, default='defaultforDB')

class ClimateScienceEntry(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=10000)
    entry = models.IntegerField(primary_key=True)
    posted_by = models.CharField(max_length=50, default='user')
    posted_date = models.CharField(max_length=20, default=( str(datetime.datetime.now().month) + ', ' + str(datetime.datetime.now().day) + ', ' + str(datetime.datetime.now().year) ) )

class EnvironmentalScienceEntry(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=10000)
    entry = models.IntegerField(primary_key=True)
    posted_by = models.CharField(max_length=50, default='user')
    posted_date = models.CharField(max_length=20, default=( str(datetime.datetime.now().month) + ', ' + str(datetime.datetime.now().day) + ', ' + str(datetime.datetime.now().year) ) )

class EcologyEntry(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=10000)
    entry = models.IntegerField(primary_key=True)
    posted_by = models.CharField(max_length=50, default='user')
    posted_date = models.CharField(max_length=20, default=( str(datetime.datetime.now().month) + ', ' + str(datetime.datetime.now().day) + ', ' + str(datetime.datetime.now().year) ) )

class TechnologyEntry(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=10000)
    entry = models.IntegerField(primary_key=True)
    posted_by = models.CharField(max_length=50, default='user')
    posted_date = models.CharField(max_length=20, default=( str(datetime.datetime.now().month) + ', ' + str(datetime.datetime.now().day) + ', ' + str(datetime.datetime.now().year) ) )
    