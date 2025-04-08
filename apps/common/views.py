from django.shortcuts import render
from rest_framework import generics 
from .serializers import *
from apps.common.models.model import FAQ
from apps.common.filter import FAQFilter
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.




class FAQView(generics.ListAPIView):
    
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    # filter_backends = []  buni yozish kerak news dan keyin
    filterset_class = FAQFilter
    filter_backends = [DjangoFilterBackend]
    # search_model = ["question"]
    pagination_class = LimitOffsetPagination

   
    @swagger_auto_schema(
        operation_summary="Get all FAQs",
        tags=["common"]
    ) 
    def get_queryset(self):
        return self.queryset.filter(active=True)


 
class FAQTagView(generics.ListAPIView):
    queryset = FAQTag.objects.all()
    serializer_class = FAQTagSerializer
    pagination_class = LimitOffsetPagination
     
    @swagger_auto_schema(
        operation_summary="Get all FAQs",
        tags=["common"]
    )
    def get_queryset(self):
        return self.queryset.all()
    


class ApplicationView(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()


class ContactView(APIView):
    def get(self , request):
        queryset = Contact.objects.all().first()
        serializers = ContactSerializer(queryset)
        return Response(serializers.data)



class FeedbackView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class ContactUserView(APIView):
    def get(self , request):
        queryset = ContactUser.objects.all().first()
        serializers = ContactSerializer(queryset , context={"request":request})
        return Response(serializers.data)


    
class SlugRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "slug"
    lookup_url_kwarg = "slug"






class CountryView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    pagination_class = LimitOffsetPagination
   # filter_backends = [filteSearchFilter]
    search_fields = ["title"]

    def get_queryset(self):
        return self.queryset.filter(active=True)


class PagesListView(generics.ListAPIView):
    queryset = Pages.objects.all()
    serializer_class = PagesSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.filter(active=True)


class PagesDetailView(SlugRetrieveAPIView):
    queryset = Pages.objects.all()
    serializer_class = PagesSerializer



