from rest_framework import serializers

from .models import Region, Category, Advertisement


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ("id", "region", "parent_id")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "title", "parent_id")


class AdvertisementSerializer(serializers.ModelSerializer):
    date_of_create = serializers.DateTimeField(format='%d.%m.%Y %H:%M')
    class Meta:
        model = Advertisement
        fields = ("id", "title", "price", "category", "date_of_create", "bearer", "previous_image")

