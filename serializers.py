from rest_framework import serializers
from .models import RingTimeModel, CallForwardingModel, RemoveCallForwardingModel, SetDefaultRingTimeModel, QueryCallForwardingModel, QueryRingTimeModel


class RingTimeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = RingTimeModel
        fields = (
            'id', 'ring_time', 'mdn'
        )


class DefaultRingTimeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = SetDefaultRingTimeModel
        fields = (
            'id', 'mdn'
        )


class CallForwardingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = CallForwardingModel
        fields = (
           'id', 'origin_mdn', 'forward_mdn'
        )


class RemoveCallForwardingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = RemoveCallForwardingModel
        fields = (
           'id', 'origin_mdn'
        )


class QueryCallForwardingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = QueryCallForwardingModel
        fields = (
            'id', 'origin_mdn', 'forward_mdn'
        )


class QueryRingTimeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = QueryRingTimeModel
        fields = (
            'id', 'mdn', 'ring_time'
        )
        