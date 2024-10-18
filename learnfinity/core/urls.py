from django.urls import path
from .views import coursedashboard, index, math_problem_view, quiz_view,ai,cys,blockchain  # Import individual views

urlpatterns = [
    path('', index, name='index'),                       # Homepage
    path('math/', math_problem_view, name='math_problem'),  # Math problem page
    path('quiz/', quiz_view, name='quiz'),
    path('course-dashboard/', coursedashboard, name='coursedashboard'),
    path('ai/', ai, name='ai'),
    path('cys/', cys, name='cys'),
    path('blockchain/', blockchain, name='blockchain'),               # Quiz page
]
