from rest_framework import serializers
from .models import EmailToken, EmailValidate


class EmailTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailToken
        fields = '__all__'


class EmailValidationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailValidate
        fields = '__all__'
