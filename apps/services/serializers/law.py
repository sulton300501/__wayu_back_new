from rest_framework import serializers

from apps.common.serializers import CountrySerializer
from apps.services.models import MigrationLaw, CountryLaw, Obligations


class MigrationLawSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = MigrationLaw
        fields = ("id", "country", "get_file")


class InsuranceSerializer(MigrationLawSerializer):
    pass


class CountryLawSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = CountryLaw
        fields = ("id", "country")


class CountryLawDetailSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = CountryLaw
        fields = ("id", "country", "description", "views_count")


class ObligationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obligations
        fields = ("id", "title", "content", "views_count")
