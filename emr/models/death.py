# Tracking file by folder pattern:  migrations
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Death(models.Model):
    person = models.ForeignKey('Person', models.DO_NOTHING, blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)
    death_datetime = models.DateTimeField(blank=True, null=True)
    death_type_concept_id = models.IntegerField(blank=True, null=True)
    cause_concept = models.ForeignKey('Concept', models.DO_NOTHING, blank=True, null=True)
    cause_source_value = models.IntegerField(blank=True, null=True)
    cause_source_concept = models.ForeignKey('Concept', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'death'
