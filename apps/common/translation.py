from modeltranslation.translator import TranslationOptions, register

from apps.common.models import model


@register(model.FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = (
        "question",
        "answer",
    )


@register(model.FAQTag)
class FAQTagTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(model.Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "address",
    )


@register(model.ContactUser)
class ContactUserTranslationOptions(TranslationOptions):
    fields = (
        "full_name",
        "position",
        "reception_days",
        "description",
    )


@register(model.Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(model.Pages)
class PagesTranslationOptions(TranslationOptions):
    fields = ("title", 'content')
