from django.urls import path

from restaurants.views import ListRestaurantView, CreateRestaurantView, ListByCategoryView, \
    RetrieveUpdateDestroyRestaurantView, ListBestRestaurantsView

urlpatterns = [
    path('', ListRestaurantView.as_view()),
    path('new/', CreateRestaurantView.as_view()),
    path('category/<int:category_id>', ListByCategoryView.as_view()),
    path('<int:restaurant_id>/', RetrieveUpdateDestroyRestaurantView.as_view()),
    path('best/', ListBestRestaurantsView.as_view())
]