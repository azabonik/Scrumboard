from rest_framework import serializers

from .models import *


class ListSerializer(serializers.ModelSerializer):

    class Meta:
        model = List


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
