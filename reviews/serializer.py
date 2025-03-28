from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ReviewUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["title", "comment"]

# 제목/댓글만 수정 가능하도록 제한
# user, restaurant 같은 필드를 수정 못 하게 하기 위해 이렇게 사용.