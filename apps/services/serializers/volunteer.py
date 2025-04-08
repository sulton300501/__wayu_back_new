from rest_framework import serializers

from apps.common.serializers import CountrySerializer, ThumbnailImageSerializer
from apps.services.models import (
    Coordinator,
    ForVolunteer,
    Opportunity,
    Volunteer,
    VolunteerResume,
)


class ForVolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForVolunteer
        fields = ("id", "title", "content")


class VolunteerResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerResume
        fields = ("id", "full_name", "email", "phone_number", "file")


class VolunteerSerializer(serializers.ModelSerializer):
    thumbnail_image = ThumbnailImageSerializer(source="image", read_only=True)

    class Meta:
        model = Volunteer
        fields = ("id", "full_name", "position", "get_image", "thumbnail_image", "email", "phone_number")


class CoordinatorSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    thumbnail_image = ThumbnailImageSerializer(source="image", read_only=True)

    class Meta:
        model = Coordinator
        fields = ("id", "country", "full_name", "position", "get_image", "thumbnail_image", "email", "phone_number")


class OpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = ("id", "title", "get_icon")
