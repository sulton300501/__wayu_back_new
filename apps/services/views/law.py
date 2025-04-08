from rest_framework import generics, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.services.models import MigrationLaw, Insurance, Obligations, CountryLaw
from apps.services.serializers.law import MigrationLawSerializer, InsuranceSerializer, ObligationsSerializer, \
    CountryLawSerializer, CountryLawDetailSerializer


class MigrationLawView(generics.ListAPIView):
    serializer_class = MigrationLawSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        queryset = MigrationLaw.objects.all()
        return queryset.filter(active=True)


class InsuranceView(generics.ListAPIView):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.filter(active=True)


class CountryLawView(generics.ListAPIView):
    queryset = CountryLaw.objects.all()
    serializer_class = CountryLawSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.filter(active=True)


class CountryLawDetailView(generics.RetrieveAPIView):
    queryset = CountryLaw.objects.all()
    serializer_class = CountryLawDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_object(self):
        obj = super().get_object()
        obj.views_count += 1
        obj.save()
        return obj
    

class ObligationsView(APIView):
    def get(self , request):
        query = Obligations.objects.first()
        try:
            query.views_count = query.views_count + 1
            query.save()
        except AttributeError:
            pass
        serializer = ObligationsSerializer(query)
        return Response(serializer.data , status=status.HTTP_200_OK)