from django.urls import path, include
from .views import Dashboard, AccountHolderAPIView

urlpatterns = [
    path('', Dashboard, name='/ome'),
    path('home/', AccountHolderAPIView.as_view())
]