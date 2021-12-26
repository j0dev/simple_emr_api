from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter


from emr.models import  Person
from emr.serializers.conceptSerializers import CustomGenderConceptSerializer, CustomRaceConceptSerializer, CustomEthnicityConceptSerializer


class PersonGenderConceptDetailView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Person.objects.select_related('gender_concept') \
        .values('gender_concept__concept_id', 'gender_concept__concept_name', 'gender_concept__domain_id').order_by(
        'gender_concept__concept_id').distinct()

    serializer_class = CustomGenderConceptSerializer
    filter_backends = [SearchFilter]
    search_fields = ['gender_concept__concept_name']


class PersonRaceDetailView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Person.objects.select_related('race_concept') \
        .values('race_concept__concept_id', 'race_concept__concept_name', 'race_concept__domain_id').order_by(
        'race_concept__concept_id').distinct()

    serializer_class = CustomRaceConceptSerializer
    filter_backends = [SearchFilter]
    search_fields = ['race_concept__concept_name']


class PersonEthnicityDetailView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Person.objects.select_related('ethnicity_concept') \
        .values('ethnicity_concept__concept_id', 'ethnicity_concept__concept_name', 'ethnicity_concept__domain_id').order_by(
        'ethnicity_concept__concept_id').distinct()

    serializer_class = CustomEthnicityConceptSerializer
    filter_backends = [SearchFilter]
    search_fields = ['ethnicity_concept__concept_name']



