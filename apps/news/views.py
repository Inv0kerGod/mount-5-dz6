from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import News
from .serializers import NewsSerizlizer
# Create your views here.

class NewsAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerizlizer
    