from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, ListCreateAPIView, DestroyAPIView

from .models import Comment

from .serializers import CommentSerializer

from django.contrib.auth import get_user_model

User = get_user_model()

class ListCommentReview (ListAPIView):
    """
    get:
    List all Comments of a specific User.
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    lookup_url_kwarg = 'user_id'

class ListCreateComment(ListCreateAPIView):
    """
    post:
    Comment on the review.
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    lookup_url_kwarg = 'review_id'

class DestroyComment(DestroyAPIView):
    """
    delete:
    Delete the Comment on the review.
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    lookup_url_kwarg = 'review_id'

