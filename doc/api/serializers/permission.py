from rest_framework import serializers
# from models import permission
from doc.models.permission import Permission

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields='__all__'