from rest_framework import serializers
from .models import Opportunity

class  Opportunityserializers(serializers.Serializer):
    class meta:
        models=Opportunity
        fields="__all__"
        
   