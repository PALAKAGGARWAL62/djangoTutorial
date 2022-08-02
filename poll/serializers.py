from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Fruit, QuantChoices

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class FruitSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, allow_blank=True)
    color = serializers.CharField(max_length=100, allow_blank=True)
    taste = serializers.CharField(max_length=100, allow_blank=True)
    price = serializers.IntegerField()
    quantity = serializers.ChoiceField(allow_blank=True, choices=QuantChoices)

    def create(self, validated_data):
        return Fruit.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.color = validated_data.get('color', instance.color)
        instance.taste = validated_data.get('taste', instance.taste)
        instance.price = validated_data.get('price', instance.price)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance

class FSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = '__all__'

        
