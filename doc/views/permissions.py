from rest_framework import viewsets, status
from doc.api.serializers.permission import PermissionSerializer
from doc.models import Permission

class PermissionViewset(viewsets.ModelViewSet):
    serializer_class= PermissionSerializer
    queryset= Permission.objects.all()
    