from django.urls import path

from .views import ListCommentReview, ListCreateComment, DestroyComment

urlpatterns = [
    path('comment/<int:user_id>/',ListCommentReview.as_view(), name='list-comment-review'),
    path('comment/new/<int:review_id>/', ListCreateComment.as_view(), name='list-create-comment'),
    path('comment/<int:review_id>/', DestroyComment.as_view(), name='destroy-comment')

]
