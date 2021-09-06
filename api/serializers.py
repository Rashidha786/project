from api.models import Dummy
from rest_framework import serializers


class RegisterS(serializers.ModelSerializer):
    class Meta:
        model = Dummy
        fields = '__all__'
