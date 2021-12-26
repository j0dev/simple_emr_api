from rest_framework import serializers
from emr.models import Person
from emr.serializers.conceptSerializers import ConceptSerializer


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ['person_id', 'birth_datetime']


class PatientDetailSerializer(serializers.ModelSerializer):
    gender_concept = ConceptSerializer(read_only=True)
    race_concept = ConceptSerializer(read_only=True)
    ethnicity_concept = ConceptSerializer(read_only=True)

    class Meta:
        model = Person
        fields = ['person_id', 'gender_concept', 'birth_datetime', 'race_concept', 'ethnicity_concept']
