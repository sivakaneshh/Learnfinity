from django.shortcuts import render
from .models import MathProblem
from django.http import JsonResponse





def index(request):
    return render(request, 'index.html')

def math_problem_view(request):
    # Assuming you have at least one problem in the database
    problem = MathProblem.objects.first()  # Get the first math problem
    return render(request, 'math_problem.html', {'problem': problem})

def quiz_view(request):
    if request.method == 'POST':
        # Process the quiz data sent via AJAX
        selected_answer = request.POST.get('answer')
        # Here you can process the answer and save it to the database
        return JsonResponse({'status': 'success', 'message': 'Answer received'})

    return render(request, 'quiz.html')

def coursedashboard(request):
    return render(request, 'coursedashboard.html')

def ai(request):
    return render(request, 'ai.html')

def cys(request):
    return render(request, 'cys.html')

def blockchain(request):
    return render(request, 'blockchain.html')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request,'regis.html')
