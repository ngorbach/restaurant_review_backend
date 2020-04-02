from django.urls import path
from .views import EmailVerification


urlpatterns = [
    path('', EmailVerification.as_view()),
   # path('/api/registration/validate/', .as_view()),
]
