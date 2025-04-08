from rest_framework import serializers
from sorl.thumbnail import get_thumbnail
from django.core.files.images import get_image_dimensions
from apps.common.models.model import *


class ThumbnailImageSerializer(serializers.Serializer):
    def to_representation(self, image):
        try:
            width , height = get_image_dimensions(image)
            request = self.context['request']
            return {
                "large": request.build_absolute_uri(
                    get_thumbnail(image , f"{int(width // 1.5)}x{int(height // 1.5)}", quality=99).url 
                ),
                "medium": request.build_absolute_uri(
                    get_thumbnail(image , f"{int(width // 2)}x{int(height // 2)}" , quality=99).url
                ),
                "small": request.build_absolute_uri(
                    get_thumbnail(image , f"{int(width // 3)}x{int(height // 3)}" , quality=99).url
                )

            }
        
        except Exception as ex:
            print(ex)


class FAQTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQTag
        fields = ("id","title")


class CountrySerializer(serializers.ModelSerializer):
    thumbnail_flag = ThumbnailImageSerializer(source="flag",read_only=True)

    class Meta:
        model = Country
        fields = ("id", "title", "get_flag", "thumbnail_flag")



class FAQSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()

    class Meta:
        model= FAQ
        fields = ("id", "question", "answer", "tags")

    def get_tags(self,obj):
        queryset =FAQTag.objects.filter(faq=obj.id)
        serializers = FAQTagSerializer(queryset , many=True)
        return serializers.data


    



class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ("id", "full_name", "phone_number", "question")


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            "id",
            "title",
            "address",
            "emails",
            "main_phone_number",
            "phones",
            "latitude",
            "longitude",
            "youtube",
            "instagram",
            "telegram",
            "twitter",
            "whatsapp",
        )


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ("id", "full_name", "phone_number", "email", "message")


class ContactUserSerializer(serializers.ModelSerializer):
    thumbnail_image = ThumbnailImageSerializer(source="image", read_only=True)

    class Meta:
        model = ContactUser
        fields = (
            "id",
            "full_name",
            "position",
            "get_image",
            "thumbnail_image",
            "phone_number",
            "email",
            "reception_days",
            "description",
        )


class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields = ("id", "title", "content", "slug")

            