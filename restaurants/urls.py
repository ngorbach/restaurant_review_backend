from django.urls import path

from restaurants.views import ListRestaurantView, ListFourRestaurantsView, CreateRestaurantView, ListByCategoryView, \
    RetrieveUpdateDestroyRestaurantView

urlpatterns = [
    path('', ListRestaurantView.as_view()),
    path('new/', CreateRestaurantView.as_view()),
    path('category/<int:category_id>', ListByCategoryView.as_view()),
    path('<int:restaurant_id>/', RetrieveUpdateDestroyRestaurantView.as_view())
]