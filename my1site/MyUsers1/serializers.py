from rest_framework import serializers
from .models import MyUsers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUsers
        fields = ('id', 'name', 'age')



