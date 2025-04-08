from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from  django.core.exceptions import ObjectDoesNotExist


from . import models
from . import serializers



class ProjectListView(generics.ListAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return self.queryset.filter(active=True)



class FeedbackProjectView(generics.CreateAPIView):
    queryset = models.FeedbackProjects.objects.all()
    serializer_class = serializers.FeedbacksSerializer




class ProjectView(APIView):
    def get(self , request , slug):
        response = {}
        try:
            introduction = models.Introduction.objects.get(project__slug=slug)
            introduction_serializer = serializers.IntroductionSerializer(introduction , context={"request":request})
            response["introduction"] = introduction_serializer.data
        except ObjectDoesNotExist:
            pass

        try:
            about_project = models.AboutProject.objects.get(project__slug=slug)
            about_project_serializer = serializers.AboutProjectSerializer(about_project , context={"request":request})
            response["about_project"] = about_project_serializer.data
        except ObjectDoesNotExist:
            pass
        try:
            goal_and_mission = models.GoalAndMission.objects.filter(project__slug=slug)
            goal_and_mission_serializer = serializers.GoalAndMissionSerializer(goal_and_mission , many=True , context={"request":request})
            response["goal_and_mission"] = goal_and_mission_serializer.data
        except ObjectDoesNotExist:
            pass
        try:
            project_document = models.ProjectDocument.objects.get(project__slug=slug)
            project_document_serializer = serializers.ProjectDocumentSerializer(
                project_document, context={"request": request}
            )
            response["project_document"] = project_document_serializer.data
        except ObjectDoesNotExist:
            pass

        try:
            document = models.Document.objects.filter(project__slug=slug)
            document_serializer = serializers.DocumentSerializer(document, many=True, context={"request": request})
            response["document"] = document_serializer.data
        except ObjectDoesNotExist:
            pass

        try:
            team_member = models.TeamMember.objects.filter(project__slug=slug)
            team_member_serializer = serializers.TeamMemberSerializer(
                team_member, many=True, context={"request": request}
            )
            response["team_member"] = team_member_serializer.data
        except ObjectDoesNotExist:
            pass

        return Response(response)

        
