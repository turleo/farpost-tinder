from rest_framework import serializers
from FarpostBackend.settings import AUTH_PASSWORD_VALIDATORS

from whiteboard.models import Advert
from profiles.serializers import UserSerializer


class AdvertSerilizer(serializers.ModelSerializer):
    author= UserSerializer
    class Meta:
        model = Advert
        fields = ['author', 'x_coordinates', 'y_coordinates', 'title', 'text']
