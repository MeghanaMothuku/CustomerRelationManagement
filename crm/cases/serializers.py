from rest_framework import serializers
from .models import Case


class CaseSerailizers(serializers.Serializer):
    class meta:
        models=Case
        fields="__all__"
        
