from django.db import models


class Contact(models.Model):
    
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    message=models.CharField(max_length=300)
    class Meta:
        db_table = "contact"
        ordering=['id']

class Hire(models.Model):
    
    jobt=models.CharField(max_length=150)
    describe=models.CharField(max_length=400)
    skills=models.CharField(max_length=100)
    exp=models.CharField(max_length=100)
    cont=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    class Meta:
        db_table = "Job"
        ordering=['id']

