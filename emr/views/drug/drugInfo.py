from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from emr.models import DrugExposure
from emr.serializers.drugSerializers import DrugDetailSerializer


class DrugDetailView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = DrugExposure.objects.all().order_by('-drug_exposure_id')
    serializer_class = DrugDetailSerializer
    filter_backends = [SearchFilter]
    search_fields = ['drug_concept__concept_name']


