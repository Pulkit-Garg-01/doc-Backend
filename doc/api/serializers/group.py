from rest_framework import serializers
# from models import group
from doc.models.group import Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields='__all__'