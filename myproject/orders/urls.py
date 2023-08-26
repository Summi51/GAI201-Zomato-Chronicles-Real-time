from django.urls import path
from . import views

urlpatterns = [
    path('chatbot/', views.chatbot, name='chatbot'),
    path('submit-feedback/', views.submit_feedback, name='submit_feedback'),
]

