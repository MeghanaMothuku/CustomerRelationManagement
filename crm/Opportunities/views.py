from django.shortcuts import render
from rest_framework import generics
from .models import Opportunity
from .serializers import Opportunityserializers

class opportunityList(generics.CreateAPIView):
    queryset=Opportunity.objects.all()
    serializer_class=Opportunityserializers

class opportunityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Opportunity.objects.all()
    serializer_class=Opportunityserializers   
