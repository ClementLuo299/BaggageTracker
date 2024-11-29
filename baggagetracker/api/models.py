from django.db import models

# Create your models here.

#Database relations

#User, null=False is default
class Usr(models.Model):
    user_id = models.CharField(max_length=100, unique=True, primary_key=True)
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50,null=True)
    lname = models.CharField(max_length=50)
    street = models.CharField(max_length=100,null=True)
    country = models.CharField(max_length=100,null=True)
    postal_code = models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=50,null=True)