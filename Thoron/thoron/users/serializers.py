from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password', '')
        instance = User.objects.create(**validated_data)
        instance.set_password(password)
        instance.save()

        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', '')
        instance = User.objects.create(**validated_data)
        instance.set_password(password)
        instance.save()

        return instance
