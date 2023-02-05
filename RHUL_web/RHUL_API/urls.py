from django.urls import path, include
from .views import Dashboard, AccountHolderAPIView, CompanyAPIView, account_holder_detail, companydetail
# from .views import Dashboard, AccountHolderAPIView, AccountAPIView, ahdetail

urlpatterns = [
    path('', Dashboard, name='/home'),
    path('home/', AccountHolderAPIView.as_view()),
    path('home/<str:name>/', account_holder_detail),
    path('company/', CompanyAPIView.as_view()),
    path('company/<str:name>/', companydetail),
    
]