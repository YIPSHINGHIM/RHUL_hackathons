from django.shortcuts import render

from rest_framework.views import APIView
from django.views.generic import DetailView
from .models import Account_Holder, CompanyInfo
from .serializers import Account_Holder_serializers, Company_serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

# from .serializers import Account_Holder_serializers
# from django.http import HttpResponse
# from rest_framework.response import Response
# from .serializers import Company_serializers
# import datetime


# Create your views here.


def Dashboard(request):
    return render(request, 'RHUL_Home.html', {'title': 'Dashboard'})


class AccountHolderAPIView(APIView):
    def get(self, request):
        modeldata = Account_Holder.objects.all()
        serializer = Account_Holder_serializers(modeldata, many=True)
        return Response(serializer.data)


class CompanyAPIView(APIView):

    def get(self, request):
        model = CompanyInfo.objects.all()
        serializer = Company_serializers(model, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def companydetail(request, name):
    try:
        company = CompanyInfo.objects.get(name=name)

    except CompanyInfo.DoesNotExist:
        return Response('No Company found!', status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Company_serializers(company)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Company_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = Company_serializers(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        company.delete()
        return Response('Company deleted', status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def account_holder_detail(request, name):
    try:
        account_holder = Account_Holder.objects.get(name=name)

    except Account_Holder.DoesNotExist:
        return Response('No account_holder found!', status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Account_Holder_serializers(account_holder)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Account_Holder_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = Account_Holder_serializers(account_holder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        account_holder.delete()
        return Response('account_holder deleted', status=status.HTTP_204_NO_CONTENT)
