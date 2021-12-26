from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter

from emr.models import Concept
from emr.serializers.conceptSerializers import ConceptSerializer


class ConceptDetailView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Concept.objects.all().order_by('-concept_id')
    serializer_class = ConceptSerializer
    filter_backends = [SearchFilter]
    search_fields = ['concept_name']