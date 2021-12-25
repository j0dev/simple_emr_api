# Tracking file by folder pattern:  migrations
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ConditionOccurrence(models.Model):
    condition_occurrence_id = models.BigIntegerField(primary_key=True)
    person = models.ForeignKey('Person', models.DO_NOTHING, blank=True, null=True)
    condition_concept = models.ForeignKey('Concept', models.DO_NOTHING, blank=True, null=True, related_name='concept_condition_occurrence_01')
    condition_start_date = models.DateField(blank=True, null=True)
    condition_start_datetime = models.DateTimeField(blank=True, null=True)
    condition_end_date = models.DateField(blank=True, null=True)
    condition_end_datetime = models.DateTimeField(blank=True, null=True)
    condition_type_concept = models.ForeignKey('Concept', models.DO_NOTHING, blank=True, null=True, related_name='concept_condition_occurrence_02')
    condition_status_concept = models.ForeignKey('Concept', models.DO_NOTHING, blank=True, null=True, related_name='concept_condition_occurrence_03')
    stop_reason = models.CharField(max_length=20, blank=True, null=True)
    provider_id = models.BigIntegerField(blank=True, null=True)
    visit_occurrence = models.ForeignKey('VisitOccurrence', models.DO_NOTHING, blank=True, null=True)
    visit_detail_id = models.BigIntegerField(blank=True, null=True)
    condition_source_value = models.CharField(max_length=50, blank=True, null=True)
    condition_source_concept = models.ForeignKey('Concept', models.DO_NOTHING, blank=True, null=True, related_name='concept_condition_occurrence_04')
    condition_status_source_value = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'condition_occurrence'
