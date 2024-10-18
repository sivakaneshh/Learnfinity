from django.urls import path
from .views import index, math_problem_view, quiz_view  # Import individual views

urlpatterns = [
    path('', index, name='index'),                       # Homepage
    path('math/', math_problem_view, name='math_problem'),  # Math problem page
    path('quiz/', quiz_view, name='quiz'),               # Quiz page
]
