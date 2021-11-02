from django.db import models

# Create your models here.

class TestingMDNS(models.Model):
    mdn = models.CharField(max_length=10)

class RingTimeModel(models.Model):
    ring_time = models.IntegerField()
    mdn = models.CharField(max_length=10)

class SetDefaultRingTimeModel(models.Model):
    mdn = models.CharField(max_length=10)

class CallForwardingModel(models.Model):
    origin_mdn = models.CharField(max_length=10)
    forward_mdn = models.CharField(max_length=10)

class RemoveCallForwardingModel(models.Model):
    origin_mdn = models.CharField(max_length=10)

class QueryCallForwardingModel(models.Model):
    origin_mdn = models.CharField(max_length=10)
    forward_mdn = models.CharField(max_length=10, default=' ')

class QueryRingTimeModel(models.Model):
    mdn = models.CharField(max_length=10)
    ring_time = models.CharField(max_length=10, default=' ')