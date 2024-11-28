from django.shortcuts import render,redirect
from django.contrib.auth import login_reqiured
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import LoanApplication
from .serializers import LoanApplicationSerializers


@login_reqiured

def apply_loan(request):
    if request.method == "POST":
        amount = request.POST.get('amount')
        repay_period = request.POST.get('repay_period')

        loan = LoanApplication.objects.create(
            applicant=request.user,
            amount=amount,
            repay_period=repay_period
        )
        messages.success(request, "Loan  application submitted successfully!")
        return redirect('Loan_history')
    return render (request, 'loans/apply_loan.html')

@login_reqiured

def admin_loan_dashboard(request):
    loans = LoanApplication.objects.filter(applicant=request.user).order_by
    ('-application_date')
    return render(request, 'loans/ loan_history.html', {'loans': loans})

#Admin view
@login_reqiured
def admin_loan_dashboard(request):
    if not request.user.is_staff:
        return redirect('home')
    loans = LoanApplication.objects.all().order_by('-apllication_date')
    return render (request, 'loans/admin_dashboard.html', {'loans': loans})

# API Views
class LoanApplicationViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = LoanApplicationSerializers

    def get_queryset(self):
        if self.request.user.is_staff:
            return LoanApplication.objects.all()
        return
    LoanApplication.objects.filter(applicant=self.request.user)

      
