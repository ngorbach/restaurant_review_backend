from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework.views import APIView
from app.settings import DEFAULT_FROM_EMAIL
from .serializer import EmailTokenSerializer, EmailValidationSerializer
from .token import TokenGen



class EmailVerification(APIView):
    permission_classes = []
    def post(self, request):
        serializer = EmailTokenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_mail(
                subject='Verification Email',
                message="Your verification key is " + TokenGen(),
                from_email=DEFAULT_FROM_EMAIL,
                recipient_list=[request.data['emailverification']],
                fail_silently=False,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class EmailValidation(APIView):
    permission_classes = []
    serializer_class = EmailValidationSerializer
    def post(self, request):
        serializer = EmailValidationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()


        """serializer = EmailValidationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)"""

