"""
定義DRF框架的序列化器類
"""
from rest_framework import serializers

class TodoInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10)
    done = serializers.BooleanField()