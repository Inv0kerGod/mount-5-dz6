from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import GeekCoin, Transaction
from .serializers import UserSerializer, GeekCoinSerializer, TransactionSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GeekCoinViewSet(viewsets.ModelViewSet):
    queryset = GeekCoin.objects.all()
    serializer_class = GeekCoinSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        sender = self.request.user
        recipient = serializer.validated_data['recipient']
        amount = serializer.validated_data['amount']

        sender_coin = GeekCoin.objects.get(user=sender)
        recipient_coin = GeekCoin.objects.get(user=recipient)

        if sender_coin.balance >= amount:
            sender_coin.balance -= amount
            recipient_coin.balance += amount
            sender_coin.save()
            recipient_coin.save()
            serializer.save(sender=sender)
    def create(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({'detail': 'Authentication credentials were not provided.'}, status=401)
        return super().create(request, *args, **kwargs)

