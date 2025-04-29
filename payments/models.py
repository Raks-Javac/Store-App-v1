from django.db import models
from core.models import User
from orders.models import Order

# Create your models here.
class Payment(models.Model):
    PENDING = 'P'
    PROCESSING = 'PR'
    SUCCESSFUL = 'S'
    FAILED = 'F'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (PROCESSING, 'Processing'),
        (SUCCESSFUL, 'Successful'),
        (FAILED, 'Failed'),
    ]


    reference = models.CharField(max_length=50)
    amount = models.IntegerField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def verify_payment(self):
        # Implement payment verification logic here
        # For example, you can call a payment gateway API to verify the payment
        # If the payment is successful, update the payment status to SUCCESSFUL
        # If the payment is failed, update the payment status to FAILED
        # Return True if the payment is successful, False otherwise
        return True

