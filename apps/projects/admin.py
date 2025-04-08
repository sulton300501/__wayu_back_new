from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from ..common.admin import ImageFieldMixin
from . import models

from core.settings.base import MODELTRANSLATION_LANGUAGES


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "short_name", "order", "active", "created_at", "updated_at")
    list_display_links = ("id", "short_name")
    ordering = ("id", "order")
    list_filter = ("active", "created_at", "updated_at")
    search_fields = ("title_uz", "title_ru", "title_en")
    exclude = ("title",)
    fieldsets = (
        (_("Asosiy 💼"), {"fields": ("logo",)}),
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
        (
            _("Qo'shimcha 🖋"),
            {
                "fields": (
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


@admin.register(models.Introduction)
class IntroductionAdmin(ImageFieldMixin, admin.ModelAdmin):
    list_display = ("id", "short_name", "project", "created_at", "updated_at")
    list_display_links = ("id", "short_name")
    ordering = ("id",)
    list_filter = ("created_at", "updated_at")
    search_fields = ("title_uz", "title_ru", "title_en", "project__title_uz", "project__title_ru", "project__title_en")
    exclude = ("title", "text")

    fieldsets = (
        (_("Asosiy 💼"), {"fields": ("project", "image", "icon")}),
        (_("O'zbekcha 🇺🇿"), {"fields": ("title_uz", "text_uz")}),
        (_("Ruscha 🇷🇺"), {"fields": ("title_ru", "text_ru")}),
        (_("Inglizcha 🇺🇸"), {"fields": ("title_en", "text_en")}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(models.AboutProject)
class AboutProjectAdmin(ImageFieldMixin, admin.ModelAdmin):
    list_display = ("id", "project", "short_name", "created_at", "updated_at")
    list_display_links = ("id", "short_name")
    ordering = ("id",)
    list_filter = ("created_at", "updated_at")
    search_fields = ("title_uz", "title_ru", "title_en", "project__title_uz", "project__title_ru", "project__title_en")
    exclude = ("title", "text")

    fieldsets = (
        (_("Asosiy 💼"), {"fields": ("project", "image", "youtube_url")}),
        (_("O'zbekcha 🇺🇿"), {"fields": ("title_uz", "text_uz")}),
        (_("Ruscha 🇷🇺"), {"fields": ("title_ru", "text_ru")}),
        (_("Inglizcha 🇺🇸"), {"fields": ("title_en", "text_en")}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(models.GoalAndMission)
class GoalAndMissionAdmin(admin.ModelAdmin):
    list_display = ("id", "project", "short_name", "order", "active", "created_at", "updated_at")
    list_display_links = ("id", "short_name")
    ordering = ("id", "order")
    list_filter = ("active", "created_at", "updated_at")
    search_fields = ("title_uz", "title_ru", "title_en", "project__title_uz", "project__title_ru", "project__title_en")
    exclude = ("title", "text")

    fieldsets = (
        (_("Asosiy 💼"), {"fields": ("project", "icon")}),
        (_("O'zbekcha 🇺🇿"), {"fields": ("title_uz", "text_uz")}),
        (_("Ruscha 🇷🇺"), {"fields": ("title_ru", "text_ru")}),
        (_("Inglizcha 🇺🇸"), {"fields": ("title_en", "text_en")}),
        (
            _("Qo'shimcha 🖋"),
            {
                "fields": (
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


@admin.register(models.Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("id", "short_title", "order", "active", "created_at", "updated_at")
    list_display_links = ("id", "short_title")
    ordering = ("id", "order")
    list_filter = ("active", "created_at", "updated_at")
    readonly_fields = ("file_size",)
    search_fields = ("title_uz", "title_ru", "title_en")
    exclude = ("title", "type")

    fieldsets = (
        (
            _("Asosiy 💼"),
            {
                "fields": (
                    "project",
                    "file",
                    "file_size",
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


@admin.register(models.ProjectDocument)
class ProjectDocumentAdmin(admin.ModelAdmin):
    list_display = ("id", "short_title", "created_at", "updated_at")
    list_display_links = ("id", "short_title")
    ordering = ("id",)
    list_filter = ("created_at", "updated_at")
    search_fields = ("title_uz", "title_ru", "title_en")
    exclude = ("title", "text")

    fieldsets = (
        (_("Asosiy 💼"), {"fields": ("project",)}),
        (_("O'zbekcha 🇺🇿"), {"fields": ("title_uz", "text_uz")}),
        (_("Ruscha 🇷🇺"), {"fields": ("title_ru", "text_ru")}),
        (_("Inglizcha 🇺🇸"), {"fields": ("title_en", "text_en")}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(models.FeedbackProjects)
class FeedbackAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    list_display = ("id", "full_name", "email", "created_at", "updated_at")
    list_display_links = ("id", "full_name")
    ordering = ("id",)
    list_filter = ("project", "created_at", "updated_at")
    readonly_fields = ("full_name", "email", "message", "project")
    search_fields = (
        "full_name",
        "email",
    )

    fieldsets = ((_("Asosiy 💼"), {"fields": ("full_name", "email", "message", "project")}),)

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(models.TeamMember)
class TeamMemberAdmin(ImageFieldMixin, admin.ModelAdmin):
    list_display = ("id", "project", "full_name", "position", "order", "created_at", "updated_at")
    list_display_links = ("id", "full_name", "project")
    ordering = ("id", "order")
    list_filter = ("created_at", "updated_at")
    search_fields = ("full_name_uz", "full_name_ru", "full_name_en", "position_uz", "position_ru", "position_en")
    exclude = (
        "full_name",
        "position",
    )
    fieldsets = (
        (_("Asosiy 💼"), {"fields": ("project", "email", "avatar")}),
        (_("O'zbekcha 🇺🇿"), {"fields": ("full_name_uz", "position_uz")}),
        (_("Ruscha 🇷🇺"), {"fields": ("full_name_ru", "position_ru")}),
        (_("Inglizcha 🇺🇸"), {"fields": ("full_name_en", "position_en")}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form
