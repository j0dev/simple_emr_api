from rest_framework import serializers
from emr.models import ConditionOccurrence
from emr.serializers.conceptSerializers import ConceptSerializer
from emr.serializers.patientSerializers import PatientSerializer
from emr.serializers.visitSerializers import VisitSerializer


class ConditionDetailSerializer(serializers.ModelSerializer):
    person = PatientSerializer(read_only=True)
    condition_concept = ConceptSerializer(read_only=True)
    visit_occurrence = VisitSerializer(read_only=True)

    class Meta:
        model = ConditionOccurrence
        fields = ['condition_occurrence_id', 'person', 'condition_concept', 'condition_start_datetime', 'condition_end_datetime', 'visit_occurrence']
