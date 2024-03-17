from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    user=models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    Firstname = models.CharField(null=True,max_length=50)
    Lastname = models.CharField(null=True,max_length=30)
    email = models.EmailField(null=True,max_length=50)
    contactno = models.CharField(max_length=12)
    age = models.PositiveIntegerField(null=True)
    occupation = models.CharField(null=True,max_length=50)

    def __str__(self):
        return self.user.username
