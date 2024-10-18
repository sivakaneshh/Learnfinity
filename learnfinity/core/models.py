from django.db import models

class MathProblem(models.Model):
    question_text = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=50)  # Store the correct answer

    def __str__(self):
        return self.question_text