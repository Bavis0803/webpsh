from rest_framework import serializers
from .models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    facode = serializers.StringRelatedField(source='code.value')
    class Meta:
        model = UserInfo
        fields = ('id', 'uid','pwd','facode','created_time')
class CodeCreateSerializer(serializers.ModelSerializer):
    code = serializers.CharField(required=False)
    class Meta:
        model = UserInfo
        fields = ['id', 'uid', 'pwd','code']
    