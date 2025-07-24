from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    repassword = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['name', 'email', 'phone_number', 'password', 'repassword']

    def validate(self, data):
        if data['password'] != data['repassword']:
            raise serializers.ValidationError({'repassword': "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('repassword')
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid email or password.")
        data['user'] = user
        return data
