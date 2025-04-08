# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView, Response
from rest_framework.parsers import FormParser , MultiPartParser

from apps.aboutus.models import (
    AboutCenterGoal,
    AboutCenterHistory,
    Header,
    Management,
    Representative,
    ResumeApplication,
    Statistic,
    Vacancy,
    WhatWeDo,
)
from apps.aboutus.serializers import (
    AboutCenterGoalSerializer,
    AboutCenterHistorySerializer,
    HeaderSerializer,
    ManagementSerializer,
    ManagementSingleSerializer,
    RepresentativeAllSerializer,
    RepresentativeSingleSerializer,
    ResumeApplicationSerializer,
    ResumeVacancySerializer,
    StatisticSerializer,
    StatusStatisticSerializer,
    VacancyAllSerializer,
    VacancySingleSerializer,
    WhatWeDoFooterSerializer,
    WhatWeDoSerializer,
)


class SlugRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "slug"
    lookup_url_kwarg = "slug"


class HeaderView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Header.objects.first()
        serializer = HeaderSerializer(queryset, context={"request": request})
        return Response(serializer.data)


class WhatWeDoView(APIView):
    def get(self, request):
        queryset = WhatWeDo.objects.first()
        serializer = WhatWeDoSerializer(queryset, context={"request": request})
        return Response(serializer.data)


class WhatWeDoFooterView(APIView):
    def get(self, request):
        query = WhatWeDo.objects.first()
        query.views_count = query.views_count + 1
        query.save()
        serializer = WhatWeDoFooterSerializer(query, context={"request": request})
        return Response(serializer.data)


class AboutCenterHistoryView(generics.ListAPIView):
    queryset = AboutCenterHistory.objects.all()
    serializer_class = AboutCenterHistorySerializer

    def get_queryset(self):
        return self.queryset.filter(active=True)


class AboutCenterGoalView(generics.ListAPIView):
    queryset = AboutCenterGoal.objects.all()
    serializer_class = AboutCenterGoalSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.filter(active=True)


class StatisticView(generics.ListAPIView):
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.filter(active=True)


class ManagementSingleView(APIView):
    def get(self, obj):
        try:
            queryset = Management.objects.filter(order=1, active=True)
            serializer = ManagementSingleSerializer(queryset, many=True)
            return Response(serializer.data)
        except Management.DoesNotExist:
            Response({"not found": 0})


class ManagementView(generics.ListAPIView):
    queryset = Management.objects.all()
    serializer_class = ManagementSerializer
    pagination_class = LimitOffsetPagination


class RepresentativeView(generics.ListAPIView):
    queryset = Representative.objects.all()
    serializer_class = RepresentativeAllSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["city_uz", "city_ru", "city_en", "country__title_uz", "country__title_ru", "country__title_en"]

    def get_queryset(self):
        return self.queryset.filter(active=True)


class RepresentativeDetailView(SlugRetrieveAPIView):
    queryset = Representative.objects.all()
    serializer_class = RepresentativeSingleSerializer


class VacancyAllView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyAllSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.filter(active=True)


class VacancySingleView(SlugRetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySingleSerializer

    def get_object(self):
        obj = super().get_object()
        obj.view_count += 1
        obj.save()
        return obj


class ResumeApplicationView(generics.CreateAPIView):
    queryset = ResumeApplication.objects.all()
    serializer_class = ResumeApplicationSerializer

    def perform_create(self, serializer):
        resume = Vacancy.objects.get(slug=self.kwargs["slug"])
        serializer.validated_data["resume"] = resume
        serializer.save()


class ResumeCreateView(generics.CreateAPIView):
    parser_classes = (MultiPartParser , FormParser)
    serializer_class = ResumeVacancySerializer
    queryset = ResumeApplication.objects.all()


class StatusStatisticView(APIView):
    def get(self, request):
        queryset = WhatWeDo.objects.first()
        serializer = StatusStatisticSerializer(queryset)
        return Response(serializer.data)
