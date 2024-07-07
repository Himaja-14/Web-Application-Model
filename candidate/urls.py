from django.urls import path
from candidate import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('homepage/', views.candidate_home, name='homepage'),
    path('dashboard/', views.candidate_dashboard, name='dashboard'),
    path('profile', views.candidate_profile, name='profile'),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)