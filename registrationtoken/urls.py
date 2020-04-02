from django.urls import path
from .views import ListEmailToken


urlpatterns = [
    path('/api/registration/', ListEmailToken.as_view()),
   # path('/api/registration/validate/', .as_view()),
]
