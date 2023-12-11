from rest_framework import serializers
from .models import Contact

class contactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

    # def create(self, validated_data):
    #     # Implement the logic to create a new Contact instance here
    #     return Contact.objects.create(**validated_data)