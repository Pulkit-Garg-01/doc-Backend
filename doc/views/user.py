from rest_framework import viewsets, status
from doc.api.serializers.user import UserSerializer
from doc.models import User

class UserViewset(viewsets.ModelViewSet):
    serializer_class= UserSerializer
    queryset= User.objects.all()
    lookup_field='username'
    