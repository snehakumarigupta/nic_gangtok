
from rest_framework import serializers
from api.models import Nicgangtok

#craete serializers here
class NicgangtokSerializer(serializers.HyperlinkedModelSerializer):
    nicgangtok_id=serializers.ReadOnlyField()
    class Meta:
        model=Nicgangtok
        fields="__all__"