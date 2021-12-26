from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny

from emr.models import VisitOccurrence
from emr.serializers.conceptSerializers import CustomVisitConceptSerializer


class VisitTypeConceptDetailView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = VisitOccurrence.objects.select_related('visit_concept') \
        .values('visit_concept__concept_id', 'visit_concept__concept_name', 'visit_concept__domain_id').order_by(
        'visit_concept__concept_id').distinct()

    serializer_class = CustomVisitConceptSerializer
    filter_backends = [SearchFilter]
    search_fields = ['visit_concept__concept_name']