from django.contrib import admin
from .models import RingTimeModel, CallForwardingModel, RemoveCallForwardingModel, SetDefaultRingTimeModel, TestingMDNS, QueryCallForwardingModel
# Register your models here.


@admin.register(TestingMDNS)
class TestingMDNSAdmin(admin.ModelAdmin):
    pass


@admin.register(RingTimeModel)
class RingTimeAdmin(admin.ModelAdmin):
    pass


@admin.register(SetDefaultRingTimeModel)
class SetDefaultRingTimeAdmin(admin.ModelAdmin):
    pass


@admin.register(CallForwardingModel)
class CallForwardingAdmin(admin.ModelAdmin):
    pass


@admin.register(RemoveCallForwardingModel)
class RemoveCallForwardingAdmin(admin.ModelAdmin):
    pass


@admin.register(QueryCallForwardingModel)
class QueryCallForwardingAdmin(admin.ModelAdmin):
    pass
