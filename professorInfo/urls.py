from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.show_info),
    path('info/find/<str:email>/', views.find_by_email),
]