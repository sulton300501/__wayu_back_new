from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from . import models, serializers
from .filters import NewsFilter

from apps.common.views import SlugRetrieveAPIView


class EventCategoriesView(generics.ListAPIView):
    queryset = models.EventCategory.objects.all()
    serializer_class = serializers.EventCategorySerializer
    pagination_class = LimitOffsetPagination



class EventsView(generics.ListAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventsSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter , DjangoFilterBackend]  # /events/?category__slug=music&date__date=2025-03-01
    filterset_fields = ["category__slug","date__date"]   #/events/?search=conference   

    def get_queryset(self):
        return self.queryset.filter(active=True)
    


class EventsDetailView(SlugRetrieveAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.views_count = obj.views_count + 1
        obj.save()
        serializer = self.get_serializer(obj)
        return Response(serializer.data , status=200)
    




class NewsTagView(generics.ListAPIView):
    queryset = models.NewsTag.objects.all()
    serializer_class = serializers.NewsTagSerializer
    pagination_class = LimitOffsetPagination



class CountryNewsView(generics.ListAPIView):
    serializer_class = serializers.CountryNewsSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["title"]

    def get_queryset(self):
        queryset = models.Country.objects.filter(news__fget=1).distinct()
        return queryset
    



class NewsCategoryListView(generics.ListAPIView):
    queryset = models.NewsCategory.objects.all()
    serializer_class = serializers.NewsCategorySerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.filter(active=True)


class NewsView(generics.ListAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializers
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = NewsFilter
    search_fields = ["title"]

    def get_queryset(self):
        return self.queryset.filter(active=True)




class NewsDetailView(SlugRetrieveAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.views_count = obj.views_count + 1
        obj.save()
        serializer = self.get_serializer(obj)
        return Response(serializer.data)
    


    

class NewsRecView(generics.ListAPIView):
    serializer_class = serializers.NewsSerializers
    pagination_class = LimitOffsetPagination
    
    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):  
            return models.News.objects.none()  # Swagger uchun bo‘sh queryset qaytarish
        
        base = get_object_or_404(models.News, slug=self.kwargs['slug'])
        return models.News.objects.filter(category=base.category_id).exclude(id=base.id).filter(active=True)
