from rest_framework import routers
from restaurants import views

router = routers.DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet)


# routers.DefaultRouter()

# 목록/생성: <basename>-list
# 상세/수정/삭제: <basename>-detail

# HTTP메서드  경로 예시            	동작	        연결 메서드             name
# GET	    /restaurants/	    목록 조회	    .list()              restaurant-list
# POST	    /restaurants/	    생성	        .create()	         restaurant-list
# GET	    /restaurants/{pk}/	단일 조회	    .retrieve()     	 restaurant-detail
# PUT	    /restaurants/{pk}/	전체 수정	    .update()	         restaurant-detail
# PATCH	    /restaurants/{pk}/	일부 수정	    .partial_update()	 restaurant-detail
# DELETE	/restaurants/{pk}/	삭제	        .destroy()           restaurant-detail

