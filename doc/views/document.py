from rest_framework import viewsets, status
# from doc.api.serializers.document import DocumentSerializer
from doc.api.serializers.document import DocumentSerializer
from doc.models import Document
# from rest_framework.permissions import IsAuthenticated

class DocumentViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class= DocumentSerializer
    queryset= Document.objects.all()