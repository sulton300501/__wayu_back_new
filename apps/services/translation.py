from modeltranslation.translator import TranslationOptions, register

from apps.services.models import library, volunteer, law, partner, career


@register(library.LibraryCatalog)
class LibraryCatalogTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(library.Book)
class BookTranslationOptions(TranslationOptions):
    fields = (
        "name",
        "author",
        "language",
        "description",
    )


@register(volunteer.ForVolunteer)
class ForVolunteerTranslationOptions(TranslationOptions):
    fields = ("title", "content")


@register(volunteer.Volunteer)
class VolunteerTranslationOptions(TranslationOptions):
    fields = ("full_name", "position",)


@register(volunteer.Coordinator)
class CoordinatorTranslationOptions(TranslationOptions):
    fields = ("full_name", "position",)


@register(volunteer.Opportunity)
class OpportunityTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(law.CountryLaw)
class MigrationTranslationOptions(TranslationOptions):
    fields = ("description",)


@register(law.Obligations)
class ObligationsTranslationOptions(TranslationOptions):
    fields = ("title", "content")


@register(partner.LegalLabAbout)
class LegalLabAboutTranslationOptions(TranslationOptions):
    fields = ("title", "description",)


@register(partner.Support)
class SupportTranslationOptions(TranslationOptions):
    fields = ("title", "description",)


@register(partner.Embassy)
class EmbassyTranslationOptions(TranslationOptions):
    fields = ("full_name", "position", "content")


@register(partner.Partnership)
class PartnershipTranslationOptions(TranslationOptions):
    fields = ("description",)


@register(partner.PartnerOrganization)
class PartnerOrganizationTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(career.CareerAbout)
class CareerAboutTranslationOptions(TranslationOptions):
    fields = ("title", "description",)


@register(career.YoungInnovator)
class YoungInnovatorTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(career.GratuitousHelp)
class GratuitousHelpTranslationOptions(TranslationOptions):
    fields = ("description",)


@register(partner.OrganizationsCategory)
class OrganizationCategoryTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(partner.PartnersCategory)
class PartnerCategoryTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(career.ServiceCategory)
class ServiceCategoryTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(career.YoungCompatriots)
class YoungCompatriotsTranslationOptions(TranslationOptions):
    fields = ("title", "content")
