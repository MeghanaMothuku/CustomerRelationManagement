from django.shortcuts import render
from .models import Case
from rest_framework import generics
from .serializers import CaseSerailizers

class CaseList(generics.CreateAPIView):
    queryset=Case.objects.all()
    serializer_class=CaseSerailizers

class CaseDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Case.objects.all()
    serializer_class=CaseSerailizers    