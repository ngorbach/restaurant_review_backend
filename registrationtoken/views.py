from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from django.core.mail import send_mail
from rest_framework.views import APIView

from app.settings import DEFAULT_FROM_EMAIL
from .serializer import EmailTokenSerializer

class EmailVerification(APIView):
    def post(self, request, **kwargs):
        serializer = EmailTokenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_mail(
                'Verfication Email',
                'Please verify your newly created Account',
                DEFAULT_FROM_EMAIL,
                request.data['email'],
                fail_silently=False,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



