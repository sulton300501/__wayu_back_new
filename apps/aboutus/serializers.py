from rest_framework import serializers

from apps.aboutus import models
from apps.common.serializers import CountrySerializer, ThumbnailImageSerializer



class HeaderSerializer(serializers.ModelSerializer):
    thumbnail_banner = ThumbnailImageSerializer(source="banner", read_only=True)

    class Meta:
        model = models.Header
        fields = ("thumbnail_banner", "get_banner", "get_icon", "title", "description")


class WhatWeDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WhatWeDo
        fields = ("short_title", "short_text", "youtube_thumbnail", "youtube_url")


class WhatWeDoFooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WhatWeDo
        fields = ("title", "content", "views_count")


class AboutCenterHistorySerializer(serializers.ModelSerializer):
    thumbnail_image = ThumbnailImageSerializer(source="image", read_only=True)

    class Meta:
        model = models.AboutCenterHistory
        fields = (
            "id",
            "title",
            "get_image",
            "thumbnail_image",
            "year",
            "title",
            "position",
            "address",
            "phone_number",
            "description",
        )


class AboutCenterGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutCenterGoal
        fields = ("description",)


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Statistic
        fields = (
            "get_icon",
            "number",
            "description",
        )


class ManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Management
        fields = (
            "full_name",
            "position",
            "get_image",
            "email",
            "phone_number",
            "work_date",
            "content",
            "biography",
        )


class ManagementSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Management
        fields = (
            "full_name",
            "position",
            "get_image",
            "email",
            "phone_number",
            "work_date",
        )


class RepresentativeAllSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = models.Representative
        fields = ("full_name", "country", "city", "get_image", "phone_number", "email", "slug", "longitude", "latitude")


class RepresentativeSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Representative
        fields = ("full_name", "position", "get_image", "email", "phone_number", "content", "longitude", "latitude")


class VacancyAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vacancy
        fields = ("title", "description", "address", "bool", "wage_from", "wage_to", "job_type", "slug")


class WorkDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkDescription
        fields = ("work_description",)


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Condition
        fields = ("condition",)


class WorkRequirement(serializers.ModelSerializer):
    class Meta:
        model = models.WorkRequirement
        fields = ("requirement",)


class VacancySingleSerializer(serializers.ModelSerializer):
    work_description = serializers.SerializerMethodField()
    condition = serializers.SerializerMethodField()
    requirement = serializers.SerializerMethodField()

    class Meta:
        model = models.Vacancy
        fields = (
            "title",
            "wage_from",
            "wage_to",
            "phone_number",
            "job_type",
            "content",
            "work_description",
            "condition",
            "requirement",
            "view_count",
        )

    def get_work_description(self, obj):
        work_description_option = models.WorkDescription.objects.filter(resume_id=obj.id)
        work_description = WorkDescriptionSerializer(work_description_option, many=True).data
        return work_description

    def get_condition(self, obj):
        condition_option = models.Condition.objects.filter(resume_id=obj.id)
        condition = ConditionSerializer(condition_option, many=True).data
        return condition

    def get_requirement(self, obj):
        requirement_option = models.WorkRequirement.objects.filter(resume_id=obj.id)
        requirement = WorkRequirement(requirement_option, many=True).data
        return requirement


class ResumeApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ResumeApplication
        fields = ("id", "phone_number", "file")


class ResumeVacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ResumeApplication
        fields = ("id", "phone_number", "full_name", "file")


class StatusStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WhatWeDo
        fields = ("status_statistic",)
