from django.urls import path

from categories.views import ListCategoryView

urlpatterns = [
    path('list/', ListCategoryView.as_view())
]
