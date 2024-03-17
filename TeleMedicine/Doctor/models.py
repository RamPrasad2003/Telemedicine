from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user=models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(null=True,max_length=50)
    last_name = models.CharField(null=True,max_length=30)
    email = models.EmailField(null=True,max_length=50)
    contact_no = models.CharField(null=True,max_length=13)
    designation = models.CharField(null=True,max_length=50)
    specialty = models.CharField(null=True,max_length=30)
    hospital=models.CharField(null=True,max_length=50)
    experience_years = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.user.username

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    publish_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment_date = models.DateField(null=True)
    appointment_time = models.TimeField(null=True)
    reason_for_visit = models.TextField(null=True,max_length=50)
    status=models.CharField(null=True,max_length=15)

    def __str__(self):
        return f"Appointment with {self.doctor} on {self.appointment_date} at {self.appointment_time}"

