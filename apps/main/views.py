from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from django.http import FileResponse





class SliderView(generics.ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.filter(active=True)
    


class PayStatisticView(generics.ListAPIView):
    queryset = models.PayStatistic.objects.all()
    serializer_class = PayStatisticSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.filter(active=True)





class BannerMenuView(generics.ListAPIView):
    queryset = models.BannerMenu.objects.all()
    serializer_class = BannerMenuSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.filter(active=True)




class HeaderMenuListView(generics.ListAPIView):
    queryset = models.HeaderMenu.objects.all().filter(parent=None)
    serializer_class = HeaderMenuSerializer
    pagination_class = LimitOffsetPagination





class UsefulLinkView(generics.ListAPIView):
    queryset = models.UsefulLink.objects.all()
    serializer_class = UsefulLinkSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.filter(active=True)
    



class QuoteView(APIView):
    def get(self , request):
        queryset = Quote.objects.all().first()
        serializers = QuoteSerializer(queryset , context={"request":request})
        return Response(serializers.data)




class CharityProjectView(APIView):
    def get(self, request):
        queryset = models.CharityProject.objects.first()
        serializer = CharityProjectSerializer(queryset, context={"request": request})
        return Response(serializer.data)
    



class NewsletterEmailView(generics.CreateAPIView):
    queryset = models.NewsletterEmail.objects.all()
    serializer_class = NewsletterEmailSerializer
    pagination_class = LimitOffsetPagination





class InstagramPhotoListView(generics.ListAPIView):
    queryset = models.InstagramPhoto.objects.all()
    serializer_class = InstagramPhotoSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return models.InstagramPhoto.objects.all().order_by("id")
    




class MusofirDonationView(generics.ListAPIView):
    serializer_class = MusofirDonationSerializer
    queryset = models.MusofirDonation.objects.filter(active=True)
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["note"]




class MusofirDonationFileDownloadView(generics.GenericAPIView):
    queryset = models.MusofirDonation.objects.all()
    serializer_class = None

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        file_path = instance.file.path 
        file_name = instance.file.name
        response = FileResponse(open(file_path , "rb"))
        response["Content-Disposition"] = "attachment; filename=%s" % file_name
        return response

