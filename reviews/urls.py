from django.urls import path
from .views import ListCreateReviewView
urlpatterns = [
    path('', ListCreateReviewView.as_view()),
]