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
    permission_classes = []
    def post(self, request):
        serializer = EmailTokenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_mail(
                subject='Verification Email',
                message='Please verify your newly created Account',
                from_email=DEFAULT_FROM_EMAIL,
                recipient_list=[request.data['emailverification']],
                fail_silently=False,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)



