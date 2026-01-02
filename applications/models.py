from django.db import models
from django.contrib.auth.models import User

class JobApplication (models.Model):
    STATUS_CHOICES = [
        ('applied','Applied'),
        ('interview','Interview'),
        ('offer','Offer'),
        ('rejected','Rejected'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='job_applications')
    company = models.CharField(max_length=200)
    
    role = models.CharField(max_length=200)

    status =  models.CharField(max_length=20,choices= STATUS_CHOICES,default='applied')

    applied_date = models.DateField()

    notes = models.TextField(blank=True)

    resume = models.FileField( upload_to='resumes/',
        blank=True,
        null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.company} - {self.name}"