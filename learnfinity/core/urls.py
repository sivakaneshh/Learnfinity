from django.urls import path
from .views import index, math_problem_view, quiz_view,ai,cys,blockchain,profile_view  # Import individual views



urlpatterns = [
    path('', index, name='index'),                       # Homepage
    path('math/', math_problem_view, name='math_problem'),  # Math problem page
    path('quiz/', quiz_view, name='quiz'),
    path('ai/', ai, name='ai'),
    path('cys/', cys, name='cys'),
    path('blockchain/', blockchain, name='blockchain'),  
    path('profile/', profile_view, name='profile'),
                
]
#from django.urls import path

#urlpatterns = [
#    path('profile/', Profile, name='profile',)  # Map /profile/ to the profile view
#]


#sample
#from django.conf import settings
#from django.conf.urls.static import static

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
