# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class InternPrjMwPawAllActivity(models.Model):
    project_name = models.CharField(max_length=64, blank=True, null=True)
    opr_status = models.CharField(max_length=64, blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    percent_share = models.FloatField(blank=True, null=True)
    drilling_activity = models.CharField(max_length=2000, blank=True, null=True)
    production_activity = models.CharField(max_length=2183, blank=True, null=True)
    seismic_activity = models.CharField(max_length=3254, blank=True, null=True)
    activity_type = models.CharField(max_length=30, blank=True, null=True)
    point_size = models.CharField(max_length=1, blank=True, null=True)
    day = models.CharField(max_length=11, blank=True, null=True)
    project_code = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intern_prj_mw_paw_all_activity'
