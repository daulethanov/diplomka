from django.urls import path, include
from .views import *
urlpatterns = [
    path('university_list', UniversityApiView.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls')),
]