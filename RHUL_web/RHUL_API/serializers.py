from rest_framework import serializers
from .models import Account_Holder, CompanyInfo


class Account_Holder_serializers(serializers.ModelSerializer):
    class Meta:
        model = Account_Holder
        field = ['name', 'social_media', 'profit', 'bank_acc', 'type', 'followers', 'about']
        exclude = ['photo', 'ts_id', 'ts_date', 'ts_amout']

class Company_serializers(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        field = ['name', 'type', 'about']
        exclude = ['total_ads']