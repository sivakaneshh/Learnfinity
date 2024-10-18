from django.shortcuts import render
from .models import MathProblem

def index(request):
    return render(request, 'index.html')

def math_problem_view(request):
    # Assuming you have at least one problem in the database
    problem = MathProblem.objects.first()  # Get the first math problem
    return render(request, 'math_problem.html', {'problem': problem})