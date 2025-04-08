from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from apps.services.models import LibraryCatalog, Book
from apps.services.serializers.library import LibraryCatalogSerializer, BookListSerializer, BookDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend


class LibraryCatalogView(generics.ListAPIView):
    queryset = LibraryCatalog.objects.all()
    serializer_class = LibraryCatalogSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.filter(active=True)


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["catalog__slug"]
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.filter(active=True)


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    lookup_field = "slug"
    lookup_url_kwarg = "slug"

    def get_object(self):
        obj = super().get_object()
        return obj


class BookRecView(generics.ListAPIView):
    serializer_class = BookListSerializer
    pagination_class = LimitOffsetPagination

    def get(self):
        base = get_object_or_404(Book , slug=self.kwargs["slug"])
        return Book.objects.filter(catalog=base.catalog_id).exclude(id=base.id).filter(active=True)