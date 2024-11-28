from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

class LoanApplication(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]
    
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField (max_digits=10, decimal_places=2)
    repay_period =  models.IntegerField(help_text="Number of months")
    interest_rate = models.DecimalField(max_digits=5,decimal_places=2, default=13.00)
    monthly_payment = models.DecimalField(max_digits=10,decimal_places=2)
    total_payment = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    application_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        #Calculate monthly payment using compound interest 
        rate = self.interest_rate  /100/ 12 
        #Monthly interest rate 
        self.monthly_payment = (self.amount *rate * (1 + rate)**self.repay_period )
        ((1 + rate)**self.repay_period -1)
        self.total_payment = self.monthly_payment *self.repay_period
        super().save(*args, **kwargs)


