from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Training(models.Model):
    training_name = models.CharField(max_length=50)
    completion_date = models.DateField()
    # TODO: Make it a duration field
    effort_in_hours = models.TimeField(null=True)
    
    def __str__(self):
        return self.training_name


class Employee(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.CharField(max_length=100, default='Robotics')
    training = models.ForeignKey(Training, on_delete=models.CASCADE, related_name='trainings')

    def __str__(self):
        return self.user.username