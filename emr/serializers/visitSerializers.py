from rest_framework import serializers

from emr.models import VisitOccurrence
from emr.serializers.conceptSerializers import ConceptSerializer
from emr.serializers.patientSerializers import PatientSerializer


class VisitSerializer(serializers.ModelSerializer):

    class Meta:
        model = VisitOccurrence
        fields = ['visit_occurrence_id', 'visit_start_datetime', 'visit_end_datetime']


class VisitDetailSerializer(serializers.ModelSerializer):
    person = PatientSerializer(read_only=True)
    visit_concept = ConceptSerializer(read_only=True)

    class Meta:
        model = VisitOccurrence
        fields = ['visit_occurrence_id', 'person', 'visit_concept', 'visit_start_datetime', 'visit_end_datetime']
