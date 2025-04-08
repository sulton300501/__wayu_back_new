from modeltranslation.translator import TranslationOptions, register


from apps.aboutus import models


@register(models.Header)
class HeaderTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(models.WhatWeDo)
class WhatWeDoTranslationOptions(TranslationOptions):
    fields = ("short_title", "short_text", "title", "content", "status_statistic")


@register(models.AboutCenterHistory)
class AboutCenterHistoryTranslationOptions(TranslationOptions):
    fields = ("title", "description", "position", "address")


@register(models.AboutCenterGoal)
class AboutCenterGoalTranslationOptions(TranslationOptions):
    fields = ("description",)


@register(models.Statistic)
class StatisticTranslationOptions(TranslationOptions):
    fields = ("description",)


@register(models.Management)
class ManagementTranslationOptions(TranslationOptions):
    fields = ("full_name", "position", "content", "biography", "work_date")


@register(models.Representative)
class RepresentativeTranslationOptions(TranslationOptions):
    fields = ("full_name", "position", "content", "city")

@register(models.WorkDescription)
class WorkDescriptionTranslationOptions(TranslationOptions):
    fields = ("work_description",)


@register(models.Condition)
class ConditionTranslationOptions(TranslationOptions):
    fields = ("condition",)


@register(models.WorkRequirement)
class WorkRequirementTranslationOptions(TranslationOptions):
    fields = ("requirement",)


@register(models.Vacancy)
class VacancyTranslationOptions(TranslationOptions):
    fields = ("title", "description", "address", "content")




