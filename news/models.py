from django.db import models
import datetime

# A News Article
class Article(models.Model):
    title = models.CharField(max_length=50)
    posted_date = models.CharField(max_length=20, default=( str(datetime.datetime.now().month) + ', ' + str(datetime.datetime.now().day) + ', ' + str(datetime.datetime.now().year) ) )
    text = models.TextField(max_length=50000)
    text_preview = models.TextField(max_length=2000)
    entry = models.IntegerField(primary_key=True)
