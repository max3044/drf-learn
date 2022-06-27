from django.shortcuts import render
from rest_framework import generics
from .models import Season
from .serializers import SeasonSerializer

# Create your views here.

class SeasonDetailApiView(generics.RetrieveAPIView):

    queryset = Season.objects
    serializer_class = SeasonSerializer

    lookup_field = "number"   # for single item 

    # custom queryset
    # def get_queryset(self): pass