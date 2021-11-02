"""bsw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import url, include
from .views import RingTimeViewSet, DefaultRingTimeViewSet, CallForwarding, RemoveCallForwarding, TestingMDNViewSet, QueryCallForwarding, QueryRingTime
from rest_framework import routers
ring_time_router = routers.DefaultRouter()
ring_time_router.register(r'set-ring-time', RingTimeViewSet)

default_ring_time_router = routers.DefaultRouter()
default_ring_time_router.register(r'default-ring-time', DefaultRingTimeViewSet)

call_forwarding_router = routers.DefaultRouter()
call_forwarding_router.register(r'set-forwarding-number', CallForwarding)

remove_forwarding_router = routers.DefaultRouter()
remove_forwarding_router.register(r'remove-forwarding-number', RemoveCallForwarding)

add_testing_mdn = routers.DefaultRouter()
add_testing_mdn.register(r'add-mdn', TestingMDNViewSet)

query_forwarding_router = routers.DefaultRouter()
query_forwarding_router.register('query-forwarding-number', QueryCallForwarding)

query_ring_time_router = routers.DefaultRouter()
query_ring_time_router.register('query-ring-time', QueryRingTime)
# mock up documentation for SI from the raw data from bsw/callforwarding/api/set-ring-time
urlpatterns = [
    url('^api/', include(ring_time_router.urls)),
    url(r'^api/', include(default_ring_time_router.urls)),
    url(r'^api/', include(call_forwarding_router.urls)),
    url(r'^api/', include(remove_forwarding_router.urls)),
    url(r'^api/', include(add_testing_mdn.urls)),
    url(r'^api/', include(query_forwarding_router.urls)),
    url(r'^api/', include(query_ring_time_router.urls))
]