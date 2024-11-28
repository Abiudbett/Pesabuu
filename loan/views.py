from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import LoanApplication
from .serializers import LoanApplicationSerializers


@login_required
def apply_loan(request):
    if request.method == "POST":
        amount = request.POST.get('amount')
        repay_period = request.POST.get('repay_period')

        loan = LoanApplication.objects.create(
            applicant=request.user,
            amount=amount,
            repay_period=repay_period
        )
        messages.success(request, "Loan application submitted successfully!")
        return redirect('loan_history')  # Ensure this matches your URL name
    return render(request, 'loans/apply_loan.html')

@login_required
def admin_loan_dashboard(request):
    if not request.user.is_staff:
        return redirect('home')  # Ensure 'home' is a valid URL name
    loans = LoanApplication.objects.all().order_by('-application_date')  # Fixed typo in 'application_date'
    return render(request, 'loans/admin_dashboard.html', {'loans': loans})

# API Views
class LoanApplicationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = LoanApplicationSerializers

    def get_queryset(self):
        if self.request.user.is_staff:
            return LoanApplication.objects.all()
        return LoanApplication.objects.filter(applicant=self.request.user)