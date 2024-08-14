from rest_framework import serializers
from django.contrib.auth.models import User
from .models import GeekCoin, Transaction

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class GeekCoinSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = GeekCoin
        fields = ['user', 'balance']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['sender', 'recipient', 'amount', 'timestamp']
