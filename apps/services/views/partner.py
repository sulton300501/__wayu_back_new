from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.common.views import SlugRetrieveAPIView
from apps.services import models
from apps.services.serializers import partner


class LegalLabAboutView(APIView):
    def get(self, request):
        query = models.LegalLabAbout.objects.first()
        serializer = partner.LegalLabAboutSerializer(query, context={"request": request})
        return Response(serializer.data)


class SupportView(generics.ListAPIView):
    queryset = models.Support.objects.all()
    serializer_class = partner.SupportSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.filter(active=True)


class OrganizationCategoryView(generics.ListAPIView):
    queryset = models.OrganizationsCategory.objects.all()
    serializer_class = partner.OrganizationCategorySerializer
    pagination_class = LimitOffsetPagination


class EmbassyView(generics.ListAPIView):
    queryset = models.Embassy.objects.all()
    serializer_class = partner.EmbassySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["organization_category__slug"]
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.filter(active=True)


class EmbassyDetailView(SlugRetrieveAPIView):
    queryset = models.Embassy.objects.all()
    serializer_class = partner.EmbassySingleSerializer


class PartnerCategoryView(generics.ListAPIView):
    queryset = models.PartnersCategory.objects.all()
    serializer_class = partner.PartnerCategorySerializer
    pagination_class = LimitOffsetPagination


class PartnershipPartnershipView(generics.ListAPIView):
    queryset = models.Partnership.objects.all()
    serializer_class = partner.PartnershipSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["partner_category__slug"]


class PartnerOrganizationView(generics.ListAPIView):
    queryset = models.PartnerOrganization.objects.all()
    serializer_class = partner.PartnerOrganizationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["partner_category__slug"]
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.filter(active=True)
