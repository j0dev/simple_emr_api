from django.db import models


class ClinicalNote(models.Model):
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clinical_note'
