from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    """Класс сериализатора для пользователя"""
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'phone', 'groups', 'password']
