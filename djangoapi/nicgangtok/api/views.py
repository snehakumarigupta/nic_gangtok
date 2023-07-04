from django.shortcuts import render
from rest_framework import viewsets
from api.models import Nicgangtok

from api.serializers import NicgangtokSerializer
# Create your views here.
class NicgangtokViewSet(viewsets.ModelViewSet):
    queryset=Nicgangtok.objects.all()

    serializer_class=NicgangtokSerializer