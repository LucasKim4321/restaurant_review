from rest_framework import serializers
from restaurants.models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"  # 모든 필드를 읽기 및 쓰기가 가능하도록 설정

# ModelSerializer는 DRF의 Serializer 클래스의 확장 버전
# Django 모델을 기반으로 자동으로 필드를 생성하고, 검증 로직도 모델에 기반해서 자동 처리