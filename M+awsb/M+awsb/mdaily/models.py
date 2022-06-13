# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime as dt, timedelta
from datetime import date

class MDailyQuerySet(models.QuerySet):
    def y2(self):
        yd =(dt.now()-timedelta(days=25)).date()
        return self.filter(checked_on__gte=yd) # make_aware(dt(2021, 12, 2)))

    def yesterday(self):
        return self.filter(checked_on__gte='2021-12-02') # make_aware(dt(2021, 12, 2)))

# class MDailyManager(models.Manager):
#     def get_queryset(self):
#        return super().get_queryset()
       #return self.filter(count__gt = 100)

class MDaily(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    imei = models.BigIntegerField()
    checked_on = models.DateTimeField()
    last_measure_at = models.DateTimeField(blank=True, null=True)
    count = models.SmallIntegerField()
    org = models.ForeignKey('MOrg', on_delete=models.DO_NOTHING, db_column='org', null=True)

    objects = MDailyQuerySet.as_manager()
    #manager = AManager()
    def __str__(self):
         return f'{self.imei} {self.org}'

    class Meta:
        managed = True
        db_table = 'M+_daily'
        verbose_name_plural = "M+DailyMeasures"

class MDevOwn(models.Model):
    imei = models.BigIntegerField(primary_key=True, unique=True)
    owner = models.ForeignKey('MOrg', on_delete=models.DO_NOTHING, db_column='owner')
    inv_id = models.ForeignKey('MInv', on_delete=models.CASCADE, null=True, db_column='inv_id')

    class Meta:
        managed = True
        db_table = 'M+_dev_own'
        verbose_name_plural = "M+DeviceOwners"

class MOrg(models.Model):
    id = models.SmallAutoField(primary_key=True, unique=True)
    org_id = models.CharField(max_length=64, default='', blank=False, db_column='org_id')
    name = models.CharField(max_length=12)
    showas = models.CharField(max_length=128, null=True)
    repid = models.IntegerField(db_column='repID')
    # Field name made lowercase. settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='repID'

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'M+_orgs'
        verbose_name_plural = "M+Orgs"

class MInv(models.Model):
    inv_id = models.SmallAutoField(primary_key=True, db_column='inv_id')
    sin = models.CharField(max_length=8)
    dated = models.DateField()
    sub_start = models.DateField(null=True)
    sub_duration = models.IntegerField(default=6)
    sub_end = models.DateField(null=True)
    sub_type = models.ForeignKey('MSub', default='ELIOT6', on_delete=models.CASCADE, db_column='sub_type')
    sub_active_rate = models.FloatField()
    sub_dorm_rate = models.FloatField()


    def __str__(self):
        return self.sin + ' dated: ' + str(self.dated)

    class Meta:
        managed = True
        db_table = 'M+_inv'
        verbose_name_plural = "M+Invoices"

class MSub(models.Model):
    name = models.CharField(primary_key=True, max_length=12)
    code = models.CharField(max_length=12)
    note = models.CharField(max_length=120)

    def __str__(self):
        return self.name + ' (' + self.note + ')'

    class Meta:
        managed = True
        db_table = 'M+_sub'
        verbose_name_plural = "M+Subscriptions"




'''    ELIOT6 ='E6'
    ELIOT12 = 'E12'
    UPFRONT = 'UP'
    PAYASUGO = 'UG'
    ELIOT24 = 'E24'
    SUB_CHOICES = [(ELIOT6, 'Eliot6'), (PAYASUGO, 'Pay as you go'),
                   (UPFRONT, '100% upfront'), (ELIOT12, 'ELIOT12'), (ELIOT24, 'ELIOT24'),]
'''
