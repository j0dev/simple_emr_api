from rest_framework import serializers
from emr.models import DrugExposure
from emr.serializers.conceptSerializers import ConceptSerializer
from emr.serializers.visitSerializers import VisitSerializer


class DrugDetailSerializer(serializers.ModelSerializer):
    drug_concept = ConceptSerializer(read_only=True)
    visit_occurrence = VisitSerializer(read_only=True)

    class Meta:
        model = DrugExposure
        fields = ['drug_exposure_id', 'drug_concept', 'drug_exposure_start_datetime', 'drug_exposure_end_datetime', 'visit_occurrence']
