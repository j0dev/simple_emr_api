from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny

from emr.models import DrugExposure
from emr.serializers.conceptSerializers import CustomDrugConceptSerializer


class DrugConceptDetailView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = DrugExposure.objects.select_related('drug_concept') \
        .values('drug_concept__concept_id', 'drug_concept__concept_name', 'drug_concept__domain_id').order_by(
        'drug_concept__concept_id').distinct()

    serializer_class = CustomDrugConceptSerializer
    filter_backends = [SearchFilter]
    search_fields = ['condition_concept__concept_name']