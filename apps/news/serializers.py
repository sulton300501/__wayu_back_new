from rest_framework import serializers

from . import models

from apps.common.serializers import CountrySerializer, ThumbnailImageSerializer


class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EventCategory
        fields = ("id","name","slug")



class EventGallerySerializer(serializers.ModelSerializer):
    thumbnail_image = ThumbnailImageSerializer(source="image" , read_only=True)
    class Meta:
        model = models.EventGallery
        fields = ("id" ,"event","image","thumbnail_image")



class EventsSerializer(serializers.ModelSerializer):
    thumbnail_image = ThumbnailImageSerializer(source="image", read_only=True)
    category = EventCategorySerializer()
    

    class Meta:
        model = models.Event
        fields = (
                  "id",
                  "category",
                  "title",
                  "thumbnail_image",
                  "get_image",
                  "address",
                  "slug",
                  "date",
                  )
        


class EventDetailSerializer(serializers.ModelSerializer):
    news_gallery = serializers.SerializerMethodField('get_images')
    category = EventCategorySerializer()
    thumbnail_image = ThumbnailImageSerializer(source="image", read_only=True)


    class Meta:
        model = models.Event
        fields = (
           "id",
            "title",
            "get_image",
            "thumbnail_image",
            "content",
            "views_count",
            "category",
            "slug",
            "address",
            "news_gallery",
        )

    def get_images(self , obj):
        return EventGallerySerializer(obj.eventgallery_set.all() , many=True , contex=self.context).data
    



class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NewsCategory
        fields = ("id", "name", "slug")


class NewsTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NewsTag
        fields = ("id", "name")


class CountryNewsSerializer(serializers.ModelSerializer):
    # country = CountrySerializer()

    class Meta:
        model = models.Country
        fields = ("id", "title")


class NewsGallerySerializer(serializers.ModelSerializer):
    thumbnail_image = ThumbnailImageSerializer(source="image", read_only=True)

    class Meta:
        model = models.NewsGallery
        fields = ("id", "news", "image", "thumbnail_image")


class NewsSerializers(serializers.ModelSerializer):
    category = NewsCategorySerializer()
    tags = NewsTagSerializer(many=True)
    country = CountrySerializer()
    thumbnail_image = ThumbnailImageSerializer(source="image", read_only=True)

    class Meta:
        model = models.News
        fields = ("id", "get_image", "thumbnail_image", "title", "category", "created_at", "country", "slug", "tags")




class NewsDetailSerializer(serializers.ModelSerializer):
    news_gallery = serializers.SerializerMethodField('get_images')
    category = NewsCategorySerializer()
    tags = NewsTagSerializer(many=True)
    thumbnail_image = ThumbnailImageSerializer(source="image", read_only=True)

    class Meta:
        model = models.News
        fields = (
            "id",
            "get_image",
            "thumbnail_image",
            "title",
            "content",
            "category",
            "created_at",
            "slug",
            "views_count",
            "tags",
            "news_gallery",
        )

    def get_images(self, obj):
        return NewsGallerySerializer(obj.newsgallery_set.all(), many=True, context=self.context).data
