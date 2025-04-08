from modeltranslation.translator import TranslationOptions , register


from . import models




@register(models.Slider)
class SliderTranslationOptions(TranslationOptions):
    fields = ("title","description")


@register(models.PayStatistic)
class PayStatisticTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(models.BannerMenu)
class BannerMenuTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "short_description",
    )


@register(models.HeaderMenu)
class HeaderMenuTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(models.UsefulLink)
class UsefulLinkTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(models.Quote)
class QuoteTagTranslationOptions(TranslationOptions):
    fields = ("quote", "full_name", "job")


@register(models.CharityProject)
class CharityProjectTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(models.MusofirDonation)
class MusofirDonationTranslationOptions(TranslationOptions):
    fields = ("note",)
