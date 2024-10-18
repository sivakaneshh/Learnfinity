from django.urls import path
from .views import index,math_problem_view

urlpatterns = [
    path('', index, name='index'),
    path('math', math_problem_view,name='math_problem')    # Map the root URL to the index view
]