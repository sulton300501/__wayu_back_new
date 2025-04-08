from rest_framework import serializers

from apps.common.serializers import ThumbnailImageSerializer
from apps.services.models import Book, LibraryCatalog


class LibraryCatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryCatalog
        fields = ("id", "title", "slug")


class BookListSerializer(serializers.ModelSerializer):
    thumbnail_image = ThumbnailImageSerializer(source="image", read_only=True)

    class Meta:
        model = Book
        fields = ("id", "name", "author", "language", "get_image", "thumbnail_image", "slug")


class BookDetailSerializer(serializers.ModelSerializer):
    thumbnail_image = ThumbnailImageSerializer(source="image", read_only=True)

    class Meta:
        model = Book
        fields = (
            "id",
            "catalog",
            "name",
            "author",
            "language",
            "get_image",
            "thumbnail_image",
            "year",
            "page_count",
            "get_file",
            "description",
        )
