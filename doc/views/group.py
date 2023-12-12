from rest_framework import viewsets, status
from doc.api.serializers.group import GroupSerializer
from doc.models import Group

class GroupViewset(viewsets.ModelViewSet):
    serializer_class= GroupSerializer
    queryset= Group.objects.all()
    
    
    
    
    
    