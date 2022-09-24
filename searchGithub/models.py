from django.db import models



class Candidate (models.Model):
    username = models.CharField(max_length=999)
    title = models.CharField(max_length=999)
    description = models.CharField(max_length=999)
    country = models.CharField(max_length=999)
    userLink = models.CharField(max_length=999)
