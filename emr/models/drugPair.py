from django.db import models


class DrugPair(models.Model):
    drug_concept_id1 = models.IntegerField(blank=True, null=True)
    drug_concept_id2 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drug_pair'
