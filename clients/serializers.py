from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Client, UnLoading


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name', 'description', )

    def create(self, validated_data):
        client = Client.objects.create(**validated_data)
        return client

class UnLoadingSerializer(serializers.ModelSerializer):
    # client = serializers.PrimaryKeyRelatedField()
    class Meta:
        model = UnLoading
        fields = ('client', 'details', 'price', 'alredy_paid', )

    def create(self, validated_data):
        client = validated_data.pop('client')
        # client_obj = Client.objects.filter(pk=client).first()
        unloading = UnLoading.objects.create(client=client, **validated_data)
        return unloading

class UnLoadingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnLoading
        fields = ('id', 'alredy_paid', )

class UnLoadingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnLoading
        fields = '__all__'
