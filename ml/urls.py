from django.urls import path
from . import views




urlpatterns = [
path('', views.home, name='index'),
path('early-diagnosis/',views.earlydiagnosis, name='earlydiagnosis'),
path('result-early-diagnosis/', views.result, name='early-result'),
path('retin-scan/', views.scan, name='scan'),
path('faqs/', views.faqs, name='faqs'),
path ('steps/', views.steps, name='steps'),
path('food-points/', views.foodpoints, name='foodpoints'),
path('sign-up/', views.signup, name='signup'),
path('sign-in/', views.signin, name='signin'),
path('chatbot/', views.chatbot, name='chatbot'),
path('logout/', views.logoutuser, name='logout'),

#arabic content
path('ar', views.homear, name='index-ar'),
path('early-diagnosis-ar/',views.earlydiagnosisar, name='earlydiagnosis-ar'),
path('result-early-diagnosis-ar/', views.resultar, name='early-result-ar'),
path('retin-scan-ar/', views.scanar, name='scan-ar'),
path('faqs-ar/', views.faqsar, name='faqs-ar'),
path ('steps-ar/', views.stepsar, name='steps-ar'),
path('food-point-ar/', views.foodpointsar, name='foodpoints-ar'),
path('sign-up-ar/', views.signupar, name='signup-ar'),
path('sign-in-ar/', views.signinar, name='signin-ar'),
path('chatbot-ar/', views.chatbotar, name='chatbot-ar'),
path('logout-ar/', views.logoutuserar, name='logout-ar'),
]