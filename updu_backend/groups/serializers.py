from rest_framework import serializers
from .models import Group
from users.models import User

class GroupSerializer(serializers.ModelSerializer):
    members = serializers.StringRelatedField(many=True, read_only=True)
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'description', 'created_by', 'members', 'created_at']

