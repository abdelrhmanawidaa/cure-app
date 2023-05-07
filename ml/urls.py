from django.urls import path
from . import views




urlpatterns = [
path('', views.home, name='index'),
path('early-diagnosis/',views.earlydiagnosis, name='earlydiagnosis'),
path('result-early-diagnosis/', views.result, name='early-result'),
path('retin-scan-fe/', views.scan, name='scan'),
path('faqs/', views.faqs, name='faqs'),
path ('steps/', views.steps, name='steps'),
path('food-points/', views.foodpoints, name='foodpoints'),
path('sign-up/', views.signup, name='signup'),
path('sign-in/', views.signin, name='signin'),
path('chatbot/', views.chatbot, name='chatbot'),
]