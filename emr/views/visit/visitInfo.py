from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from emr.models import VisitOccurrence
from emr.serializers.visitSerializers import VisitDetailSerializer


class VisitDetailView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = VisitOccurrence.objects.all().order_by('-visit_occurrence_id')
    serializer_class = VisitDetailSerializer
    filter_backends = [SearchFilter]
    search_fields = ['visit_concept__concept_name']
