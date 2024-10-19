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

def profile_view(request):
    return render(request,'profile.html')

def video(request):
    return render(request,'video.html')

def puzzle(request):
    return render(request,'puzzle.html')

def story(request):
    return render(request,'story.html')





#sample
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile  # Assuming you have a UserProfile model to store user data

@login_required
def update_profile(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        country_code = request.POST['country_code']
        
        # Update user profile data
        user_profile = request.user.profile  # Assuming user has a related profile
        user_profile.name = name
        user_profile.email = email
        user_profile.phone = phone
        user_profile.country_code = country_code
        user_profile.save()

        messages.success(request, 'Your profile has been updated.')
        return redirect('profile_page')  # Redirect back to the profile page

    return render(request, 'profile.html', {'user': request.user})
