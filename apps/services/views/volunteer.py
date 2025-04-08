from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.services.models import (
    Coordinator,
    ForVolunteer,
    Opportunity,
    Volunteer,
    VolunteerResume,
)
from apps.services.serializers.volunteer import (
    CoordinatorSerializer,
    ForVolunteerSerializer,
    OpportunitySerializer,
    VolunteerResumeSerializer,
    VolunteerSerializer,
)


class ForVolunteerView(APIView):
    def get(self, request):
        query = ForVolunteer.objects.first()
        serializer = ForVolunteerSerializer(query, context={"request": request})
        return Response(serializer.data)


class VolunteerResumeCreateView(generics.CreateAPIView):
    queryset = VolunteerResume.objects.all()
    serializer_class = VolunteerResumeSerializer


class VolunteerView(generics.ListAPIView):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.filter(active=True)


class CoordinatorView(generics.ListAPIView):
    queryset = Coordinator.objects.all()
    serializer_class = CoordinatorSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.filter(active=True)


class OpportunityView(generics.ListAPIView):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.filter(active=True)
