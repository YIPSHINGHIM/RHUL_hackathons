from rest_framework import serializers
from .models import Account_Holder


class Account_Holder_serializers(serializers.ModelSerializer):
    class Meta:
        model = Account_Holder
        field = ['name', 'social_media', 'profit', 'bank_acc', 'type', 'followers', 'about']
        exclude = ['photo']
