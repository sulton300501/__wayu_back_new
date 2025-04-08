from modeltranslation.translator import TranslationOptions, register

from . import models


@register(models.Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(models.Introduction)
class CalendarPlanTranslationOptions(TranslationOptions):
    fields = ("title", "text",)


@register(models.AboutProject)
class AboutProjectTranslationOptions(TranslationOptions):
    fields = ("title", "text",)


@register(models.GoalAndMission)
class GoalAndMissionTranslationOptions(TranslationOptions):
    fields = ("title", "text",)


@register(models.Document)
class DocumentTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(models.ProjectDocument)
class ProjectDocumentTranslationOptions(TranslationOptions):
    fields = ("title", "text",)


@register(models.TeamMember)
class TeamMemberTranslationOptions(TranslationOptions):
    fields = ("full_name", "position",)
