from django.urls import path
from .views import index  # Ensure you are importing the view correctly

urlpatterns = [
    path('', index, name='index'),  # Map the root URL to the index view
]