from rest_framework import serializers
from employee_registration.models import *


class EmpDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmpDetails
        fields="__all__"

        
class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Position
        fields="__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields="__all__"

class ShopingSerializer(serializers.ModelSerializer):
    class Meta:
        model=ShoopingCheckOut
        fields="__all__"