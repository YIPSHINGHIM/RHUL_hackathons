from django.urls import path, include
from .views import Dashboard, AccountHolderAPIView, CompanyAPIView, companydetail
from .views import Dashboard, AccountHolderAPIView, CompanyAPIView

urlpatterns = [
    path('', Dashboard, name='/home'),
    path('home/', AccountHolderAPIView.as_view()),
    path('company/', CompanyAPIView.as_view()),
    path('company/<str:name>/', companydetail)
]