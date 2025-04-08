from rest_framework import serializers

from apps.common.serializers import CountrySerializer, ThumbnailImageSerializer
from apps.services.models import (
    Embassy,
    LegalLabAbout,
    OrganizationsCategory,
    PartnerOrganization,
    PartnersCategory,
    Partnership,
    Support,
)


class LegalLabAboutSerializer(serializers.ModelSerializer):
    thumbnail_youtube = ThumbnailImageSerializer(source="youtube_thumbnail", read_only=True)

    class Meta:
        model = LegalLabAbout
        fields = (
            "id",
            "title",
            "description",
            "get_youtube_thumbnail",
            "thumbnail_youtube",
            "youtube_url",
        )


class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = (
            "id",
            "title",
            "description",
        )


class OrganizationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationsCategory
        fields = ("id", "title", "slug")


class EmbassySerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    thumbnail_image = ThumbnailImageSerializer(source="image", read_only=True)

    class Meta:
        model = Embassy
        fields = (
            "id",
            "country",
            "full_name",
            "position",
            "get_image",
            "thumbnail_image",
            "phone_number",
            "email",
            "slug",
        )


class EmbassySingleSerializer(serializers.ModelSerializer):
    thumbnail_image = ThumbnailImageSerializer(source="image", read_only=True)

    class Meta:
        model = Embassy
        fields = (
            "full_name",
            "position",
            "get_image",
            "thumbnail_image",
            "email",
            "phone_number",
            "content",
            "longitude",
            "latitude",
        )


class PartnerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnersCategory
        fields = ("id", "title", "slug")


class PartnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partnership
        fields = (
            "id",
            "description",
        )


class PartnerOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerOrganization
        fields = (
            "partner_category",
            "title",
            "get_logo",
            "site_name",
        )
