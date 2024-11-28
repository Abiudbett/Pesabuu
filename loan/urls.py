from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoanApplicationViewSet, ApplyLoanView, AdminLoanDashboardView  # Correct import

router = DefaultRouter()
router.register(r'loans', LoanApplicationViewSet, basename='Loan')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apply/', ApplyLoanView.as_view(), name='apply_loan'),
    path('history/', LoanHistoryView.as_view(), name='loan_history'),
    path('admin-dashboard/', AdminLoanDashboardView.as_view(), name='admin_loan_dashboard'),
    path('api/', include(router.urls)),
]