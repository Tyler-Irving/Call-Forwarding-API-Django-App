from django.shortcuts import render
from django.contrib import messages
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import  Response
from rest_framework import status
from .models import RingTimeModel, CallForwardingModel, RemoveCallForwardingModel, SetDefaultRingTimeModel, QueryCallForwardingModel, QueryRingTimeModel, TestingMDNS
from .forms import CallForwardingForm
from .view_functions import update_ring_time, set_callforwarding, remove_callforwarding, query_callforwarding, query_ring_time
from .serializers import RingTimeSerializer, CallForwardingSerializer, RemoveCallForwardingSerializer, DefaultRingTimeSerializer, QueryCallForwardingSerializer, QueryRingTimeSerializer
from .settings import ENVIRONMENT
# Create your views here.


class RingTimeViewSet(ModelViewSet):
    queryset = RingTimeModel.objects.all().order_by('id')
    serializer_class = RingTimeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if ENVIRONMENT == "TEST":
            testing_mdns = [i.mdn for i in TestingMDNS.objects.all()]
            if serializer.validated_data["mdn"] not in testing_mdns:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        update_ring_time(serializer.validated_data["mdn"], str(serializer.validated_data["ring_time"]))
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DefaultRingTimeViewSet(ModelViewSet):
    queryset = SetDefaultRingTimeModel.objects.all().order_by('id')
    serializer_class = DefaultRingTimeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if ENVIRONMENT == "TEST":
            testing_mdns = [i.mdn for i in TestingMDNS.objects.all()]
            if serializer.validated_data["mdn"] not in testing_mdns:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        update_ring_time(serializer.validated_data["mdn"], "30")
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CallForwarding(ModelViewSet):
    queryset = CallForwardingModel.objects.all().order_by('id')
    serializer_class = CallForwardingSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if ENVIRONMENT == "TEST":
            testing_mdns = [i.mdn for i in TestingMDNS.objects.all()]
            if serializer.validated_data["origin_mdn"] not in testing_mdns or serializer.validated_data["forward_mdn"] not in testing_mdns:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        set_callforwarding(serializer.validated_data["origin_mdn"], serializer.validated_data["forward_mdn"])
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class RemoveCallForwarding(ModelViewSet):
    queryset = RemoveCallForwardingModel.objects.all().order_by('id')
    serializer_class = RemoveCallForwardingSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if ENVIRONMENT == "TEST":
            testing_mdns = [i.mdn for i in TestingMDNS.objects.all()]
            if serializer.validated_data["origin_mdn"] not in testing_mdns:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        remove_callforwarding(serializer.validated_data["origin_mdn"])
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class QueryCallForwarding(ModelViewSet):
    queryset = QueryCallForwardingModel.objects.all().order_by('id')
    serializer_class = QueryCallForwardingSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if ENVIRONMENT == "TEST":
            testing_mdns = [i.mdn for i in TestingMDNS.objects.all()]
            if serializer.validated_data["origin_mdn"] not in testing_mdns:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        forwarding_mdn = query_callforwarding(serializer.validated_data['origin_mdn'])
        serializer.validated_data["forward_mdn"] = forwarding_mdn
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class QueryRingTime(ModelViewSet):
    queryset = QueryRingTimeModel.objects.all().order_by('id')
    serializer_class = QueryRingTimeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if ENVIRONMENT == "TEST":
            testing_mdns = [i.mdn for i in TestingMDNS.objects.all()]
            if serializer.validated_data["mdn"] not in testing_mdns:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        ring_time = query_ring_time(serializer.validated_data['mdn'])
        serializer.validated_data['ring_time'] = ring_time
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)