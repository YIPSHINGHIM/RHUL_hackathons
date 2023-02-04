from django.urls import path, include
from .views import Dashboard, AccountHolderAPIView, CompanyAPIView, companydetail

urlpatterns = [
    path('', Dashboard, name='/ome'),
    path('home/', AccountHolderAPIView.as_view()),
    path('company/', CompanyAPIView.as_view()),
    path('company/<str:name>/', companydetail)
]