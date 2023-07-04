from django.contrib import admin
from django.urls import path,include
from api.views import NicgangtokViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'nicgangtok',NicgangtokViewSet)


urlpatterns = [
    path('',include(router.urls))
    
]
