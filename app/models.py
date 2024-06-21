from django.db import models

# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    # Image ka liya pillow download krna pare ga
    profile_img = models.ImageField(upload_to='static/image/',null=True,blank=True)
