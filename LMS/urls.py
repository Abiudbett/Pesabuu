"""
URL configuration for LMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from loan.views import LoanApplicationViewSet, LoanHistoryView, AdminLoanDashboardView

router = DefaultRouter()
router.register(r'loans', LoanApplicationViewSet, basename='Loan')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apply/', LoanHistoryView.as_view(), name='apply_loan'),
    path('history/', LoanHistoryView.as_view(), name='loan_history'),
    path('admin-dashboard/', AdminLoanDashboardView.as_view(), name='admin_loan_dashboard'),
    path('api/', include(router.urls)),py
]

