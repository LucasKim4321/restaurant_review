from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


# ModelViewSet
# Django REST Framework(DRF)에서 CRUD 기능을 자동으로 제공

# HTTP메서드	URL 예시             동작
# GET	    /restaurants/	    목록 조회 (List)
# POST	    /restaurants/	    새 항목 생성 (Create)
# GET	    /restaurants/1/	    상세 조회 (Retrieve)
# PUT	    /restaurants/1/	    전체 수정 (Update)
# PATCH	    /restaurants/1/	    일부 수정 (Partial Update)
# DELETE	/restaurants/1/	    삭제 (Destroy)

# 작동 조건
# 모델이 존재해야 함
# Serializer가 정의되어 있어야 함
# urls.py에서 ViewSet을 라우팅 해야 함