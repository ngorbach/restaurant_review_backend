from django.urls import path
from .views import ListCreateReviewView, ListReviewsUser, GetUpdateDeleteReview


urlpatterns = [
    path('', ListCreateReviewView.as_view()),
    path('<int:review_id>/', GetUpdateDeleteReview.as_view()),
    path('user/<int:user_id>/', ListReviewsUser.as_view(), name='list-reviews-user'),
    path('restaurant/<int:restaurant_id>/', ListReviewsUser.as_view(), name='list-reviews-restaurant'),
]
