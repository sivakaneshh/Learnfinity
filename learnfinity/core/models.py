from django.db import models

class MathProblem(models.Model):
    question_text = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=50)  # Store the correct answer

    def __str__(self):
        return self.question_text

#sample
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    country_code = models.CharField(max_length=5, default='+1')  # Example default country code

    def __str__(self):
        return self.user.username
