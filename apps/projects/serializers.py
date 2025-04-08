from rest_framework import serializers

from . import models

from apps.common.serializers import ThumbnailImageSerializer


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = ("id", "title", "get_logo", "slug")


class IntroductionSerializer(serializers.ModelSerializer):
    thumbnail_image = ThumbnailImageSerializer(source="image", read_only=True)

    class Meta:
        model = models.Introduction
        fields = ("id", "project", "title", "text", "get_image", "thumbnail_image", "get_icon")


class AboutProjectSerializer(serializers.ModelSerializer):
    thumbnail_image = ThumbnailImageSerializer(source="image", read_only=True)

    class Meta:
        model = models.AboutProject
        fields = ("id", "title", "text", "get_image", "thumbnail_image", "youtube_url")


class GoalAndMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GoalAndMission
        fields = ("id", "title", "text", "get_icon")


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Document
        fields = ("id", "project", "title", "get_file", "file_size", "type")


class ProjectDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectDocument
        fields = ("id", "title", "text")


class TeamMemberSerializer(serializers.ModelSerializer):
    thumbnail_avatar = ThumbnailImageSerializer(source="avatar", read_only=True)

    class Meta:
        model = models.TeamMember
        fields = ("id", "project", "full_name", "email", "position", "get_avatar", "thumbnail_avatar")


class FeedbacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FeedbackProjects
        fields = ("full_name", "email", "message", "project")
