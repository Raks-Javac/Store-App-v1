from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.generics import CreateAPIView,RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Payment
from .serializers import  GetReferenceSerializer, VerifyPaymentSerializer

# Create your views here.
class GetReferencePaymentViewSet(CreateAPIView, GenericViewSet):
    queryset = Payment.objects.all()
    serializer_class = GetReferenceSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class InitiatePaymentViewSet(CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = GetReferenceSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)



class VerifyPaymentViewSet(CreateAPIView, GenericViewSet):
    serializer_class = VerifyPaymentSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'reference'
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        payment = Payment.objects.get(reference=ref)
        headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=201, headers=headers)
        verified = payment.verify_payment()
        if verified:
            data = {
                "status": "success",
                "message": "payment verified successfully",
                "data": None
            }
            return Response(data)
        data = {
            "status": "failed",
            "message": "payment not verified",
            "data": None
        }
        return Response(data)
                


