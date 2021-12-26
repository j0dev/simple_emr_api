from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny

from emr.models import ConditionOccurrence
from emr.serializers.conceptSerializers import CustomConditionConceptSerializer


class ConditionConceptDetailView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = ConditionOccurrence.objects.select_related('condition_concept') \
        .values('condition_concept__concept_id', 'condition_concept__concept_name', 'condition_concept__domain_id').order_by(
        'condition_concept__concept_id').distinct()

    serializer_class = CustomConditionConceptSerializer
    filter_backends = [SearchFilter]
    search_fields = ['condition_concept__concept_name']
