from rest_framework import serializers
from .models import Content


class ContentSerializer(serializers.Serializer):
    width = serializers.IntegerField()
    heigth = serializers.IntegerField()


    def create(self, validated_data):
        return Content.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.width = validated_data.get('width', instance.width)
        instance.heigth = validated_data.get(
            'heigth', instance.heigth)
        instance.save()
        return instance
