from rest_framework import serializers
from apps.common.serializers import ThumbnailImageSerializer
from . import models



class SliderSerializer(serializers.ModelSerializer):
    thumbnail_image = ThumbnailImageSerializer(source="image" , read_only=True)

    class Meta:
        model = models.Slider
        fields = ("id", "title", "description", "get_image", "thumbnail_image")





class PayStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PayStatistic
        fields = ("id", "title", "get_icon", "count")


class BannerMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BannerMenu
        fields = ("id", "title", "get_icon", "path")


class SubHeaderMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HeaderMenu
        fields = (
            "id",
            "title",
            "path",
        )



class HeaderMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HeaderMenu
        fields = (
            "id",
            "title",
            "path",
        )

    
    def get_fields(self):
        fields = super(HeaderMenuSerializer , self).get_fields()
        fields["children"] = SubHeaderMenuSerializer(many=True , required=False)
        return fields





class UsefulLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UsefulLink
        fields = (
            "id",
            "title",
            "get_logo",
            "site_name",
        )


class QuoteSerializer(serializers.ModelSerializer):
    thumbnail_image = ThumbnailImageSerializer(source="image", read_only=True)

    class Meta:
        model = models.Quote
        fields = ("id", "full_name", "quote", "job", "get_image", "thumbnail_image")


class CharityProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CharityProject
        fields = ("id", "title", "description", "get_logo", "app_store_url", "google_play_url")


class NewsletterEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NewsletterEmail
        fields = ("id", "email")


class InstagramPhotoSerializer(serializers.ModelSerializer):
    thumbnail_img = ThumbnailImageSerializer(source="img", read_only=True)

    class Meta:
        model = models.InstagramPhoto
        fields = ("id", "link", "get_img", "thumbnail_img")





class MusofirDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MusofirDonation
        fields = ("id", "amount", "date", "note", "get_file")

