from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.aboutus.admin import SingletonAdminMixin
from apps.common.admin import ImageFieldMixin
from apps.services.models import career, law, library, partner, volunteer
from core.settings.base import MODELTRANSLATION_LANGUAGES


@admin.register(library.LibraryCatalog)
class LibraryCatalogAdmin(admin.ModelAdmin):
    list_display = ("id", "short_title", "order", "active", "created_at", "updated_at")
    ordering = ("id", "order")
    list_display_links = ("id", "short_title")
    list_filter = ("active", "created_at", "updated_at")
    search_fields = ("title_uz", "title_ru", "title_en")
    exclude = ("title",)
    fieldsets = (
        (
            _("O'zbekcha 🇺🇿"),
            {
                "fields": (
                    "title_uz",
                    "slug_from_lang",
                    "slug",
                )
            },
        ),
        (_("Ruscha 🇷🇺"), {"fields": ("title_ru",)}),
        (_("Inglizcha 🇺🇸"), {"fields": ("title_en",)}),
        (_("Qo'shimcha 🖋"), {"fields": ("order", "active")}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(library.Book)
class BookAdmin(ImageFieldMixin, admin.ModelAdmin):
    list_display = ("id", "short_name", "author", "order", "active", "created_at", "updated_at")
    ordering = ("id", "order")
    list_display_links = ("id", "short_name")
    list_filter = ("active", "created_at", "updated_at")
    search_fields = ("name_uz", "name_ru", "name_en", "author_uz", "author_ru", "author_en")
    exclude = ("name", "author", "language", "description")
    fieldsets = (
        (
            _("Asosiy 💼"),
            {
                "fields": (
                    "catalog",
                    "image",
                    "year",
                    "page_count",
                    "file",
                )
            },
        ),
        (
            _("O'zbekcha 🇺🇿"),
            {"fields": ("name_uz", "slug_from_lang", "slug", "author_uz", "language_uz", "description_uz")},
        ),
        (_("Ruscha 🇷🇺"), {"fields": ("name_ru", "author_ru", "language_ru", "description_ru")}),
        (_("Inglizcha 🇺🇸"), {"fields": ("name_en", "author_en", "language_en", "description_en")}),
        (_("Qo'shimcha 🖋"), {"fields": ("order", "active")}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(volunteer.ForVolunteer)
class ForVolunteerAdmin(SingletonAdminMixin, admin.ModelAdmin):
    list_display = ("id", "short_title", "created_at", "updated_at")
    list_display_links = ("id", "short_title")
    exclude = ("title", "content")
    fieldsets = (
        (
            _("O'zbekcha 🇺🇿"),
            {
                "fields": (
                    "title_uz",
                    "content_uz",
                )
            },
        ),
        (
            _("Ruscha 🇷🇺"),
            {
                "fields": (
                    "title_ru",
                    "content_ru",
                )
            },
        ),
        (
            _("Inglizcha 🇺🇸"),
            {
                "fields": (
                    "title_en",
                    "content_en",
                )
            },
        ),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(volunteer.VolunteerResume)
class VolunteerResumeAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    list_display = ("id", "full_name", "active", "created_at", "updated_at")
    list_display_links = ("id", "full_name")
    list_filter = ("active", "created_at", "updated_at")
    search_fields = ("full_name",)
    readonly_fields = (
        "full_name",
        "email",
        "phone_number",
        "file",
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(volunteer.Volunteer)
class VolunteerAdmin(ImageFieldMixin, admin.ModelAdmin):
    list_display = ("id", "short_title", "position", "order", "active", "created_at", "updated_at")
    ordering = ("id", "order")
    list_display_links = ("id", "short_title")
    list_filter = ("active", "created_at", "updated_at")
    search_fields = ("full_name_uz", "full_name_ru", "full_name_en", "position_uz", "position_ru", "position_en")
    exclude = (
        "full_name",
        "position",
    )
    fieldsets = (
        (_("Asosiy 💼"), {"fields": ("email", "image", "phone_number")}),
        (
            _("O'zbekcha 🇺🇿"),
            {
                "fields": (
                    "full_name_uz",
                    "position_uz",
                )
            },
        ),
        (
            _("Ruscha 🇷🇺"),
            {
                "fields": (
                    "full_name_ru",
                    "position_ru",
                )
            },
        ),
        (
            _("Inglizcha 🇺🇸"),
            {
                "fields": (
                    "full_name_en",
                    "position_en",
                )
            },
        ),
        (_("Qo'shimcha 🖋"), {"fields": ("order", "active")}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(volunteer.Coordinator)
class CoordinatorAdmin(ImageFieldMixin, admin.ModelAdmin):
    list_display = ("id", "short_title", "position", "order", "active", "created_at", "updated_at")
    ordering = ("id", "order")
    list_display_links = ("id", "short_title")
    list_filter = ("country", "active", "created_at", "updated_at")
    search_fields = ("full_name_uz", "full_name_ru", "full_name_en", "position_uz", "position_ru", "position_en")
    exclude = (
        "full_name",
        "position",
    )
    fieldsets = (
        (
            _("Asosiy 💼"),
            {
                "fields": (
                    "country",
                    "email",
                    "image",
                    "phone_number",
                )
            },
        ),
        (
            _("O'zbekcha 🇺🇿"),
            {
                "fields": (
                    "full_name_uz",
                    "position_uz",
                )
            },
        ),
        (
            _("Ruscha 🇷🇺"),
            {
                "fields": (
                    "full_name_ru",
                    "position_ru",
                )
            },
        ),
        (
            _("Inglizcha 🇺🇸"),
            {
                "fields": (
                    "full_name_en",
                    "position_en",
                )
            },
        ),
        (_("Qo'shimcha 🖋"), {"fields": ("order", "active")}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(volunteer.Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "order",
        "active",
        "created_at",
        "updated_at",
    )
    ordering = ("id", "order")
    list_display_links = ("id", "title")
    list_filter = ("active", "created_at", "updated_at")
    search_fields = ("title_uz", "title_ru", "title_en")
    exclude = ("title",)
    fieldsets = (
        (_("Asosiy 💼"), {"fields": ("icon",)}),
        (_("O'zbekcha 🇺🇿"), {"fields": ("title_uz",)}),
        (_("Ruscha 🇷🇺"), {"fields": ("title_ru",)}),
        (_("Inglizcha 🇺🇸"), {"fields": ("title_en",)}),
        (_("Qo'shimcha 🖋"), {"fields": ("order", "active")}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(law.MigrationLaw)
class MigrationLawAdmin(admin.ModelAdmin):
    list_display = ("id", "country", "order", "active", "created_at", "updated_at")
    ordering = ("id", "order")
    list_display_links = ("id", "country")
    list_filter = ("country", "active", "created_at", "updated_at")
    search_fields = ("country__title_uz", "country__title_ru", "country__title_en")
    fieldsets = (
        (
            _("Asosiy 💼"),
            {
                "fields": (
                    "country",
                    "file",
                    "order",
                    "active",
                )
            },
        ),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(law.Insurance)
class InsuranceAdmin(MigrationLawAdmin):
    pass


@admin.register(law.CountryLaw)
class CountryLawAdmin(admin.ModelAdmin):
    list_display = ("id", "country", "views_count", "order", "active", "created_at", "updated_at")
    ordering = ("id", "order")
    list_display_links = ("id", "country")
    search_fields = ("country__title_uz", "country__title_ru", "country__title_en")
    list_filter = ("country", "active", "created_at", "updated_at")
    readonly_fields = ("views_count",)
    exclude = ("description",)
    fieldsets = (
        (_("Asosiy 💼"), {"fields": ("country", "views_count")}),
        (_("O'zbekcha 🇺🇿"), {"fields": ("description_uz",)}),
        (_("Ruscha 🇷🇺"), {"fields": ("description_ru",)}),
        (_("Inglizcha 🇺🇸"), {"fields": ("description_en",)}),
        (_("Qo'shimcha 🖋"), {"fields": ("order", "active")}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(law.Obligations)
class ObligationsAdmin(SingletonAdminMixin, admin.ModelAdmin):
    list_display = ("id", "short_title", "views_count", "created_at", "updated_at")
    list_display_links = (
        "id",
        "short_title",
    )
    exclude = ("title", "content")
    fieldsets = (
        (_("O'zbekcha 🇺🇿"), {"fields": ("title_uz", "content_uz")}),
        (_("Ruscha 🇷🇺"), {"fields": ("title_ru", "content_ru")}),
        (_("Inglizcha 🇺🇸"), {"fields": ("title_en", "content_en")}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(partner.LegalLabAbout)
class LegalLabAboutAdmin(ImageFieldMixin, SingletonAdminMixin, admin.ModelAdmin):
    list_display = ("id", "short_title", "created_at", "updated_at")
    list_display_links = (
        "id",
        "short_title",
    )
    exclude = ("title", "description")
    fieldsets = (
        (_("Asosiy 💼"), {"fields": ("youtube_thumbnail", "youtube_url")}),
        (_("O'zbekcha 🇺🇿"), {"fields": ("title_uz", "description_uz")}),
        (_("Ruscha 🇷🇺"), {"fields": ("title_ru", "description_ru")}),
        (_("Inglizcha 🇺🇸"), {"fields": ("title_en", "description_en")}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(partner.Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = ("id", "short_title", "order", "active", "created_at", "updated_at")
    list_display_links = (
        "id",
        "short_title",
    )
    ordering = ("id", "order")
    search_fields = (
        "title_uz",
        "title_ru",
        "title_en",
    )
    list_filter = ("active", "created_at", "updated_at")
    exclude = ("title", "description")
    fieldsets = (
        (_("Asosiy 💼"), {"fields": ("icon",)}),
        (_("O'zbekcha 🇺🇿"), {"fields": ("title_uz", "description_uz")}),
        (_("Ruscha 🇷🇺"), {"fields": ("title_ru", "description_ru")}),
        (_("Inglizcha 🇺🇸"), {"fields": ("title_en", "description_en")}),
        (_("Qo'shimcha 🖋"), {"fields": ("order", "active")}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(partner.Embassy)
class EmbassyAdmin(ImageFieldMixin, admin.ModelAdmin):
    list_display = (
        "id",
        "full_name",
        "organization_category",
        "country",
        "position",
        "active",
        "created_at",
        "updated_at",
    )
    list_display_links = (
        "id",
        "full_name",
    )
    search_fields = ("full_name_uz", "full_name_ru", "full_name_en")
    list_filter = ("country", "organization_category", "active", "created_at", "updated_at")
    exclude = ("full_name", "position", "content")
    fieldsets = (
        (
            _("Asosiy 💼"),
            {
                "fields": (
                    "country",
                    "organization_category",
                    "image",
                    "phone_number",
                    "email",
                    "active",
                    "location_url",
                    "latitude",
                    "longitude",
                )
            },
        ),
        (_("O'zbekcha 🇺🇿"), {"fields": ("full_name_uz", "slug_from_lang", "slug", "position_uz", "content_uz")}),
        (_("Ruscha 🇷🇺"), {"fields": ("full_name_ru", "position_ru", "content_ru")}),
        (_("Inglizcha 🇺🇸"), {"fields": ("full_name_en", "position_en", "content_en")}),
    )
    readonly_fields = ("latitude", "longitude")

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(partner.Partnership)
class PartnershipAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "partner_category",
        "short_description",
        "created_at",
        "updated_at",
    )
    list_display_links = (
        "id",
        "partner_category",
    )
    search_fields = ("description_uz", "description_ru", "description_en")
    list_filter = ("partner_category", "created_at", "updated_at")
    exclude = ("description",)
    fieldsets = (
        (_("Asosiy 💼"), {"fields": ("partner_category",)}),
        (_("O'zbekcha 🇺🇿"), {"fields": ("description_uz",)}),
        (_("Ruscha 🇷🇺"), {"fields": ("description_ru",)}),
        (_("Inglizcha 🇺🇸"), {"fields": ("description_en",)}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(partner.PartnerOrganization)
class PartnerOrganizationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "short_title",
        "partner_category",
        "order",
        "active",
        "created_at",
        "updated_at",
    )
    list_display_links = ("id", "partner_category", "short_title")
    search_fields = ("title_uz", "title_ru", "title_en")
    ordering = ("id", "order")
    list_filter = ("partner_category", "active", "created_at", "updated_at")
    exclude = ("title",)
    fieldsets = (
        (_("Asosiy 💼"), {"fields": ("partner_category", "logo", "site_name")}),
        (_("O'zbekcha 🇺🇿"), {"fields": ("title_uz",)}),
        (_("Ruscha 🇷🇺"), {"fields": ("title_ru",)}),
        (_("Inglizcha 🇺🇸"), {"fields": ("title_en",)}),
        (_("Qo'shimcha 🖋"), {"fields": ("order", "active")}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(career.ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "short_title",
        "order",
        "created_at",
        "updated_at",
    )
    list_display_links = ("id", "short_title")
    search_fields = ("title_uz", "title_ru", "title_en")
    ordering = ("id", "order")
    list_filter = ("created_at", "updated_at")
    exclude = ("title",)
    fieldsets = (
        (_("Asosiy 💼"), {"fields": ("icon", "path")}),
        (_("O'zbekcha 🇺🇿"), {"fields": ("title_uz",)}),
        (_("Ruscha 🇷🇺"), {"fields": ("title_ru",)}),
        (_("Inglizcha 🇺🇸"), {"fields": ("title_en",)}),
        (_("Qo'shimcha 🖋"), {"fields": ("order",)}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(career.CareerAbout)
class CareerAboutAdmin(ImageFieldMixin, SingletonAdminMixin, admin.ModelAdmin):
    list_display = (
        "id",
        "short_title",
        "created_at",
        "updated_at",
    )
    list_display_links = ("id", "short_title")
    exclude = (
        "title",
        "description",
    )
    fieldsets = (
        (_("Asosiy 💼"), {"fields": ("youtube_thumbnail", "youtube_url")}),
        (
            _("O'zbekcha 🇺🇿"),
            {
                "fields": (
                    "title_uz",
                    "description_uz",
                )
            },
        ),
        (
            _("Ruscha 🇷🇺"),
            {
                "fields": (
                    "title_ru",
                    "description_ru",
                )
            },
        ),
        (
            _("Inglizcha 🇺🇸"),
            {
                "fields": (
                    "title_en",
                    "description_en",
                )
            },
        ),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(career.YoungInnovator)
class YoungInnovatorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "active",
        "created_at",
        "updated_at",
    )
    list_display_links = ("id", "title")
    search_fields = ("title_uz", "title_ru", "title_en")
    list_filter = ("active", "created_at", "updated_at")
    exclude = ("title",)
    fieldsets = (
        (_("O'zbekcha 🇺🇿"), {"fields": ("title_uz",)}),
        (_("Ruscha 🇷🇺"), {"fields": ("title_ru",)}),
        (_("Inglizcha 🇺🇸"), {"fields": ("title_en",)}),
        (_("Qo'shimcha 🖋"), {"fields": ("active",)}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(career.PhotoGallery)
class PhotoGalleryAdmin(ImageFieldMixin, admin.ModelAdmin):
    list_display = (
        "id",
        "image",
        "active",
        "created_at",
        "updated_at",
    )
    list_display_links = ("id",)
    list_filter = ("active", "created_at", "updated_at")
    fieldsets = ((_("Asosiy 💼"), {"fields": ("image", "active")}),)

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(career.PhotoGalleryCompatriots)
class PhotoGalleryCompatriotsAdmin(PhotoGalleryAdmin):
    pass


@admin.register(career.GratuitousHelp)
class GratuitousHelpAdmin(SingletonAdminMixin, admin.ModelAdmin):
    list_display = (
        "id",
        "short_description",
        "created_at",
        "updated_at",
    )
    list_display_links = ("id", "short_description")
    exclude = ("description",)
    fieldsets = (
        (_("O'zbekcha 🇺🇿"), {"fields": ("description_uz",)}),
        (_("Ruscha 🇷🇺"), {"fields": ("description_ru",)}),
        (_("Inglizcha 🇺🇸"), {"fields": ("description_en",)}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(career.GoogleForm)
class GoogleFormAdmin(SingletonAdminMixin, admin.ModelAdmin):
    list_display = ("id", "google_form")
    list_display_links = ("id", "google_form")

    fieldsets = ((_("Asosiy 💼"), {"fields": ("google_form",)}),)


@admin.register(partner.OrganizationsCategory)
class OrganizationsCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "created_at",
        "updated_at",
    )
    list_display_links = ("id", "title")
    search_fields = ("title_uz", "title_ru", "title_en")
    list_filter = ("created_at", "updated_at")
    exclude = ("title",)
    fieldsets = (
        (
            _("O'zbekcha 🇺🇿"),
            {
                "fields": (
                    "title_uz",
                    "slug_from_lang",
                    "slug",
                )
            },
        ),
        (_("Ruscha 🇷🇺"), {"fields": ("title_ru",)}),
        (_("Inglizcha 🇺🇸"), {"fields": ("title_en",)}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(partner.PartnersCategory)
class PartnersCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at")
    list_display_links = ("id", "title")
    search_fields = ("title_uz", "title_ru", "title_en")
    list_filter = ("created_at", "updated_at")
    exclude = ("title",)
    fieldsets = (
        (
            _("O'zbekcha 🇺🇿"),
            {
                "fields": (
                    "title_uz",
                    "slug_from_lang",
                    "slug",
                )
            },
        ),
        (_("Ruscha 🇷🇺"), {"fields": ("title_ru",)}),
        (_("Inglizcha 🇺🇸"), {"fields": ("title_en",)}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(career.YoungCompatriots)
class YoungCompatriotsAdmin(SingletonAdminMixin, admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at")
    list_display_links = ("id", "title")
    exclude = ("title", "content")
    fieldsets = (
        (_("O'zbekcha 🇺🇿"), {"fields": ("title_uz", "content_uz")}),
        (_("Ruscha 🇷🇺"), {"fields": ("title_ru", "content_ru")}),
        (_("Inglizcha 🇺🇸"), {"fields": ("title_en", "content_en")}),
    )
