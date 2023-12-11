from rest_framework import serializers
from .models import AccountUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountUser
        fields = ["username","email","password","confirm_password","mobile_number"]

    def create(self, validated_data):
        user = AccountUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            confirm_password=validated_data['confirm_password'],
            mobile_number = validated_data["mobile_number"],
            
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
    

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()





    