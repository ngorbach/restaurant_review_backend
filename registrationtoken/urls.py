from django.urls import path
from .views import EmailVerification, EmailValidation

urlpatterns = [
    path('', EmailVerification.as_view()),
    path('validation/', EmailValidation.as_view()),
]
