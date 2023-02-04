from django.urls import path, include
from .views import Dashboard, AccountHolderAPIView, CompanyAPIView

urlpatterns = [
    path('', Dashboard, name='/ome'),
    path('home/', AccountHolderAPIView.as_view()),
    path('company/', CompanyAPIView.as_view()),
    path('company/<int:id>/', CompanyAPIView.as_view())
]