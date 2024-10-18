from django.db import models

class MathProblem(models.Model):
    question_text = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=50)  # Store the correct answer

    def __str__(self):
        return self.question_text
    


    #sample
    from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    progress = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s Profile"
