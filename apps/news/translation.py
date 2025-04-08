from modeltranslation.translator import TranslationOptions, register

from . import models


@register(models.EventCategory)
class EventCategoryOptions(TranslationOptions):
    fields = ["name"]


@register(models.Event)
class EventTranslationOptions(TranslationOptions):
    fields = ("title", "content")


@register(models.NewsCategory)
class NewsCategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(models.NewsTag)
class NewsTagOptions(TranslationOptions):
    fields = ["name"]


@register(models.News)
class NewsTranslationOptions(TranslationOptions):
    fields = ("title", "content")

