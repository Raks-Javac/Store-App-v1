from rest_framework import serializers
from .models import Payment

class GetReferenceSerializer(serializers.ModelSerializer):
    reference = serializers.CharField(max_length=50, read_only=True)
    class Meta:
        model = Payment
        fields = ['reference','order','amount']

class VerifyPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['reference']

