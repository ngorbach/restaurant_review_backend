from django.urls import path
from .views import ListCreateReview
urlpatterns = [
    path('', ListCreateReview.as_view()),
]

