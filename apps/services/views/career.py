from rest_framework import generics, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.services import models
from apps.services.serializers import career


class CareerAboutView(APIView):
    def get(self, request):
        query = models.CareerAbout.objects.first()
        serializer = career.CareerAboutSerializer(query, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class YoungInnovatorView(generics.ListAPIView):
    queryset = models.YoungInnovator.objects.all()
    serializer_class = career.YoungInnovatorSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.filter(active=True)


class PhotoGalleryView(generics.ListAPIView):
    queryset = models.PhotoGallery.objects.all()
    serializer_class = career.PhotoGallerySerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.filter(active=True)


class PhotoGalleryCompatriotsView(generics.ListAPIView):
    queryset = models.PhotoGalleryCompatriots.objects.all()
    serializer_class = career.PhotoGalleryCompatriotsSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.filter(active=True)


class GratuitousHelpView(APIView):
    def get(self, request):
        query = models.GratuitousHelp.objects.first()
        serializer = career.GratuitousHelpSerializer(query, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ServiceCategoryView(generics.ListAPIView):
    queryset = models.ServiceCategory.objects.all()
    serializer_class = career.ServiceCategorySerializer
    pagination_class = LimitOffsetPagination


class YoungCompatriotsView(APIView):
    def get(self, request):
        query = models.YoungCompatriots.objects.first()
        serializer = career.YoungCompatriotsSerializer(query, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class GoogleFormView(APIView):
    def get(self, request):
        query = models.GoogleForm.objects.first()
        serializer = career.GoogleFormSerializer(query, context={"request": request})
        return Response(serializer.data)
