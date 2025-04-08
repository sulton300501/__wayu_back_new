from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from mptt.admin import DraggableMPTTAdmin

from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from . import models

from apps.common.admin import ImageFieldMixin, SingletonAdminMixin
from core.settings.base import MODELTRANSLATION_LANGUAGES

# @admin.register(models.Slider)
# class SliderAdmin(ImageFieldMixin, SingletonAdminMixin, admin.ModelAdmin):
#     list_display = (
#         "id",
#         "short_title",
#         "active",
#         "created_at",
#         "updated_at",
#     )
#     ordering = ("id",)
#     list_display_links = ("id", "short_title")
#     list_filter = ("active", "created_at", "updated_at")
#     search_fields = ("title_uz", "title_ru", "title_en")
#     exclude = (
#         "title",
#         "description",
#     )
#     fieldsets = (
#         (
#             _("Asosiy 💼"),
#             {"fields": ("image",)},
#         ),
#         (
#             _("O'zbekcha 🇺🇿"),
#             {
#                 "fields": (
#                     "title_uz",
#                     "description_uz",
#                 )
#             },
#         ),
#         (
#             _("Ruscha 🇷🇺"),
#             {
#                 "fields": (
#                     "title_ru",
#                     "description_ru",
#                 )
#             },
#         ),
#         (
#             _("Inglizcha 🇺🇸"),
#             {
#                 "fields": (
#                     "title_en",
#                     "description_en",
#                 )
#             },
#         ),
#     )
#
#     def get_form(self, request, obj=None, change=False, **kwargs):
#         form = super().get_form(request, obj, change, **kwargs)
#         for value in form.base_fields:
#             if value[-2::] in MODELTRANSLATION_LANGUAGES:
#                 form.base_fields[value].required = True
#         return form


@admin.register(models.PayStatistic)
class PayStatisticAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "short_title",
        "count",
        "active",
        "order",
        "created_at",
        "updated_at",
    )
    ordering = ("id", "title", "order")
    list_display_links = ("id", "short_title")
    list_filter = ("active", "created_at", "updated_at")
    search_fields = ("title_uz", "title_ru", "title_en")
    exclude = ("title",)
    fieldsets = (
        (_("Asosiy 💼"), {"fields": ("count", "icon")}),
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


@admin.register(models.BannerMenu)
class BannerMenuAdmin(admin.ModelAdmin):
    list_display = ("id", "short_title", "path", "order", "active", "created_at", "updated_at")
    list_filter = ("active", "created_at", "updated_at")
    ordering = ("id", "order")
    list_display_links = ("id", "short_title")
    search_fields = ("title_uz", "title_ru", "title_en", "path")
    exclude = ("title", "short_description")
    fieldsets = (
        (_("Asosiy 💼"), {"fields": ("path", "icon")}),
        (_("O'zbekcha 🇺🇿"), {"fields": ("title_uz", "short_description_uz")}),
        (_("Ruscha 🇷🇺"), {"fields": ("title_ru", "short_description_ru")}),
        (_("Inglizcha 🇺🇸"), {"fields": ("title_en", "short_description_en")}),
        (_("Qo'shimcha 🖋"), {"fields": ("order", "active")}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(models.HeaderMenu)
class HeaderMenuAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    mptt_level_indent = 40
    search_fields = ("title_uz", "title_ru", "title_en")
    exclude = ("title",)
    fieldsets = (
        (
            _("Asosiy 💼"),
            {"fields": ("parent", "path", "order")},
        ),
        (_("O'zbekcha 🇺🇿"), {"fields": ("title_uz",)}),
        (_("Ruscha 🇷🇺"), {"fields": ("title_ru",)}),
        (_("Inglizcha 🇺🇸"), {"fields": ("title_en",)}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(models.UsefulLink)
class UsefulLinkAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "short_title",
        "active",
        "order",
        "created_at",
        "updated_at",
    )
    ordering = ("id", "title", "order")
    list_display_links = ("id", "short_title")
    list_filter = ("active", "created_at", "updated_at")
    search_fields = ("title_uz", "title_ru", "title_en")
    exclude = ("title",)
    fieldsets = (
        (
            _("Asosiy 💼"),
            {
                "fields": (
                    "logo",
                    "site_name",
                )
            },
        ),
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


@admin.register(models.Quote)
class QuoteAdmin(ImageFieldMixin, SingletonAdminMixin, admin.ModelAdmin):
    list_display = ("short_full_name", "short_quote", "created_at", "updated_at")
    list_display_links = ("short_full_name",)
    exclude = ("quote", "full_name", "job")
    fieldsets = (
        (
            _("Asosiy 💼"),
            {"fields": ("image",)},
        ),
        (
            _("O'zbekcha 🇺🇿"),
            {
                "fields": (
                    "full_name_uz",
                    "quote_uz",
                    "job_uz",
                )
            },
        ),
        (
            _("Ruscha 🇷🇺"),
            {
                "fields": (
                    "full_name_ru",
                    "quote_ru",
                    "job_ru",
                )
            },
        ),
        (
            _("Inglizcha 🇺🇸"),
            {
                "fields": (
                    "full_name_en",
                    "quote_en",
                    "job_en",
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


@admin.register(models.CharityProject)
class CharityProjectAdmin(SingletonAdminMixin, admin.ModelAdmin, DynamicArrayMixin):
    list_display = ("id", "short_title", "created_at", "updated_at")
    list_display_links = ("id", "short_title")
    exclude = (
        "title",
        "description",
    )
    fieldsets = (
        (
            _("Asosiy 💼"),
            {"fields": ("logo", "app_store_url", "google_play_url")},
        ),
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


@admin.register(models.NewsletterEmail)
class NewsletterEmailAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    list_display = (
        "id",
        "email",
        "created_at",
    )
    list_filter = ("created_at",)
    list_display_links = ("id", "email")
    readonly_fields = ("email",)
    ordering = ("id",)
    search_fields = ("email",)


@admin.register(models.InstagramPhoto)
class InstagramPhotoAdmin(ImageFieldMixin, admin.ModelAdmin):
    list_display = ("id", "link", "img")


@admin.register(models.MusofirDonation)
class MusofirDonationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "note",
        "active",
        "created_at",
        "updated_at",
    )
    ordering = ("id",)
    list_display_links = ("id", "note")
    list_filter = ("created_at", "updated_at")
    search_fields = ("note_uz", "note_ru", "note_en")
    exclude = ("note",)
    fieldsets = (
        (
            _("Asosiy 💼"),
            {"fields": ("amount", "date", "file", "active")},
        ),
        (_("O'zbekcha 🇺🇿"), {"fields": ("note_uz",)}),
        (_("Ruscha 🇷🇺"), {"fields": ("note_ru",)}),
        (_("Inglizcha 🇺🇸"), {"fields": ("note_en",)}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form
