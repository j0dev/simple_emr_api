from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from emr.models import ConditionOccurrence
from emr.serializers.conditionSerializers import ConditionDetailSerializer


class ConditionDetailView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = ConditionOccurrence.objects.all().order_by('-condition_occurrence_id')
    serializer_class = ConditionDetailSerializer
    filter_backends = [SearchFilter]
    search_fields = ['condition_concept__concept_name']


