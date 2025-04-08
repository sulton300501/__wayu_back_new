from rest_framework import serializers

from apps.common.serializers import ThumbnailImageSerializer
from apps.services.models import (
    CareerAbout,
    GoogleForm,
    GratuitousHelp,
    PhotoGallery,
    ServiceCategory,
    YoungCompatriots,
    YoungInnovator,
)


class CareerAboutSerializer(serializers.ModelSerializer):
    thumbnail_youtube = ThumbnailImageSerializer(source="youtube_thumbnail", read_only=True)

    class Meta:
        model = CareerAbout
        fields = (
            "id",
            "title",
            "description",
            "get_youtube_thumbnail",
            "thumbnail_youtube",
            "youtube_url",
        )


class YoungInnovatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoungInnovator
        fields = (
            "id",
            "title",
        )


class PhotoGallerySerializer(serializers.ModelSerializer):
    thumbnail_image = ThumbnailImageSerializer(source="image", read_only=True)

    class Meta:
        model = PhotoGallery
        fields = ("id", "get_image", "thumbnail_image")


class PhotoGalleryCompatriotsSerializer(PhotoGallerySerializer):
    pass


class GratuitousHelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = GratuitousHelp
        fields = ("id", "description")


class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = (
            "id",
            "title",
            "icon",
            "path",
        )


class YoungCompatriotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoungCompatriots
        fields = ("id", "title", "content")


class GoogleFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleForm
        fields = ("id", "google_form")
