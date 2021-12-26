from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from emr.models import Person
from emr.serializers.patientSerializers import PatientDetailSerializer


class PatientDetailView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Person.objects.all().order_by('-person_id')
    serializer_class = PatientDetailSerializer
    filter_backends = [SearchFilter]
    search_fields = ['gender_concept__concept_name']
