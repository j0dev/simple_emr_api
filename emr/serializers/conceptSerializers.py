from rest_framework import serializers

from emr.models import Concept, Person


class ConceptSerializer(serializers.ModelSerializer):

    class Meta:
        model = Concept
        fields = ['concept_id', 'concept_name', 'domain_id']


class CustomGenderConceptSerializer(serializers.Serializer):
    gender_concept__concept_id = serializers.IntegerField()
    gender_concept__concept_name = serializers.CharField(max_length=255)
    gender_concept__domain_id = serializers.CharField(max_length=20)


class CustomRaceConceptSerializer(serializers.Serializer):
    race_concept__concept_id = serializers.IntegerField()
    race_concept__concept_name = serializers.CharField(max_length=255)
    race_concept__domain_id = serializers.CharField(max_length=20)

class CustomEthnicityConceptSerializer(serializers.Serializer):
    ethnicity_concept__concept_id = serializers.IntegerField()
    ethnicity_concept__concept_name = serializers.CharField(max_length=255)
    ethnicity_concept__domain_id = serializers.CharField(max_length=20)
