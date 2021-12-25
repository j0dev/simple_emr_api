# Tracking file by folder pattern:  migrations
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class VisitOccurrence(models.Model):
    visit_occurrence_id = models.BigIntegerField(primary_key=True)
    person = models.ForeignKey('Person', models.DO_NOTHING, blank=True, null=True)
    visit_concept = models.ForeignKey('Concept', models.DO_NOTHING, blank=True, null=True, related_name='concept_visit_01')
    visit_start_date = models.DateField(blank=True, null=True)
    visit_start_datetime = models.DateTimeField(blank=True, null=True)
    visit_end_date = models.DateField(blank=True, null=True)
    visit_end_datetime = models.DateTimeField(blank=True, null=True)
    visit_type_concept = models.ForeignKey('Concept', models.DO_NOTHING, blank=True, null=True, related_name='concept_visit_02')
    provider_id = models.BigIntegerField(blank=True, null=True)
    care_site_id = models.BigIntegerField(blank=True, null=True)
    visit_source_value = models.CharField(max_length=50, blank=True, null=True)
    visit_source_concept = models.ForeignKey('Concept', models.DO_NOTHING, blank=True, null=True, related_name='concept_visit_03')
    admitted_from_concept_id = models.IntegerField(blank=True, null=True)
    admitted_from_source_value = models.CharField(max_length=50, blank=True, null=True)
    discharge_to_source_value = models.CharField(max_length=50, blank=True, null=True)
    discharge_to_concept = models.ForeignKey('Concept', models.DO_NOTHING, blank=True, null=True, related_name='concept_visit_04')
    preceding_visit_occurrence = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visit_occurrence'
