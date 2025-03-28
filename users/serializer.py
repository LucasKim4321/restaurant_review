
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nickname', 'email', 'is_staff', 'is_superuser', 'profile_image']


class UserUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(source='password', write_only=True)

    class Meta:
        model = User
        fields = ['nickname', 'password']

    def update(self, instance, validated_data):
        # 닉네임 업데이트
        instance.nickname = validated_data.get('nickname', instance.nickname)

        # 비밀번호 업데이트
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)  # set_password()를 사용하여 비밀번호를 해싱해서 저장

        instance.save()
        return instance
