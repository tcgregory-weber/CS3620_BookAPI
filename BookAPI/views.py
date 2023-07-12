from django.shortcuts import render
from rest_framework import viewsets
from .models import BookData
from .serializers import BookSerializer

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='History')
    serializer_class = BookSerializer

class FantasyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Fantasy')
    serializer_class = BookSerializer

class HistoricalFictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Historical Fiction')
    serializer_class = BookSerializer

class ScienceFictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Science Fiction')
    serializer_class = BookSerializer

class SocialScienceFictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Social Science Fiction')
    serializer_class = BookSerializer

class BiographyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Biography')
    serializer_class = BookSerializer

class ThrillerViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Thriller')
    serializer_class = BookSerializer

class SelfHelpViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Self-Help')
    serializer_class = BookSerializer

class MemoirViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Memoir')
    serializer_class = BookSerializer

class NonFictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Non-Fiction')
    serializer_class = BookSerializer