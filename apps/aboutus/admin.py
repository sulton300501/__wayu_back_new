from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.aboutus import models
from apps.common.admin import ImageFieldMixin
from core.settings.base import MODELTRANSLATION_LANGUAGES


class SingletonAdminMixin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.all_objects().count() > 0:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        return self.model.objects.all_objects()


@admin.register(models.Header)
class HeaderAdmin(ImageFieldMixin, SingletonAdminMixin, admin.ModelAdmin):
    list_display = (
        "id",
        "short_title",
        "created_at",
        "updated_at",
    )
    search_fields = ("title", "description")
    list_filter = ("created_at",)
    list_display_links = ("id", "short_title")
    exclude = (
        "title",
        "description",
    )
    fieldsets = (
        (_("Asosiy 💼"), {"fields": ("banner", "icon")}),
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


@admin.register(models.WhatWeDo)
class WhatWeDoAdmin(ImageFieldMixin, SingletonAdminMixin, admin.ModelAdmin):
    list_display = ("id", "short_title_func", "short_text", "views_count", "created_at", "updated_at")
    search_fields = (
        "short_title_uz",
        "short_text_uz",
        "short_title_ru",
        "short_text_ru",
        "short_title_en",
        "short_text_en",
    )
    list_display_links = ("id", "short_title_func")
    exclude = ("short_title", "short_text", "title", "content", "status_statistic")
    fieldsets = (
        (_("Asosiy 💼"), {"fields": ("youtube_thumbnail", "youtube_url", "views_count")}),
        (
            _("O'zbekcha 🇺🇿"),
            {"fields": ("short_title_uz", "title_uz", "short_text_uz", "content_uz", "status_statistic_uz")},
        ),
        (
            _("Ruscha 🇷🇺"),
            {"fields": ("short_title_ru", "title_ru", "short_text_ru", "content_ru", "status_statistic_ru")},
        ),
        (
            _("Inglizcha 🇺🇸"),
            {"fields": ("short_title_en", "title_en", "short_text_en", "content_en", "status_statistic_en")},
        ),
    )
    readonly_fields = ("views_count",)

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(models.AboutCenterHistory)
class AboutCenterHistoryAdmin(ImageFieldMixin, admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "created_at",
        "updated_at",
        "active",
    )
    list_display_links = (
        "id",
        "title",
    )
    exclude = ("title", "description", "address", "position")
    search_fields = ("title", "description")
    list_filter = ("active", "created_at", "year")
    fieldsets = (
        (_("Asosiy 💼"), {"fields": ("year", "image", "phone_number")}),
        (
            _("O'zbekcha 🇺🇿"),
            {
                "fields": (
                    "title_uz",
                    "position_uz",
                    "address_uz",
                    "description_uz",
                )
            },
        ),
        (
            _("Ruscha 🇷🇺"),
            {
                "fields": (
                    "title_ru",
                    "position_ru",
                    "address_ru",
                    "description_ru",
                )
            },
        ),
        (
            _("Inglizcha 🇺🇸"),
            {
                "fields": (
                    "title_en",
                    "position_en",
                    "address_en",
                    "description_en",
                )
            },
        ),
        (_("Qo'shimcha 🖋"), {"fields": ("active",)}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(models.AboutCenterGoal)
class AboutCenterGoalAdmin(admin.ModelAdmin):
    list_display = ("id", "short_title", "created_at", "updated_at", "order", "active")
    list_display_links = ("id", "short_title")
    list_filter = ("active", "created_at", "updated_at")
    search_fields = ("description",)
    exclude = ("description",)
    fieldsets = (
        (
            _("O'zbekcha 🇺🇿"),
            {"fields": ("description_uz",)},
        ),
        (
            _("Ruscha 🇷🇺"),
            {"fields": ("description_ru",)},
        ),
        (
            _("Inglizcha 🇺🇸"),
            {"fields": ("description_en",)},
        ),
        (_("Qo'shimcha 🖋"), {"fields": ("active", "order")}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(models.Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ("id", "short_title", "number", "active", "order", "created_at", "updated_at")
    list_filter = ("number", "active")
    list_display_links = (
        "id",
        "short_title",
    )
    search_fields = ("description",)
    exclude = ("description",)
    fieldsets = (
        (_("Asosiy 💼"), {"fields": ("icon", "number")}),
        (
            _("O'zbekcha 🇺🇿"),
            {"fields": ("description_uz",)},
        ),
        (
            _("Ruscha 🇷🇺"),
            {"fields": ("description_ru",)},
        ),
        (
            _("Inglizcha 🇺🇸"),
            {"fields": ("description_en",)},
        ),
        (_("Qo'shimcha 🖋"), {"fields": ("order", "active")}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(models.Management)
class ManagementAdmin(ImageFieldMixin, admin.ModelAdmin):
    list_display = ("id", "short_title", "position", "email", "phone_number", "active", "created_at", "updated_at")
    search_fields = ("full_name", "position", "content", "biography")
    list_display_links = ("id", "short_title", "position")
    list_filter = ("active", "created_at", "updated_at")
    exclude = ("full_name", "position", "content", "biography", "work_date")
    fieldsets = (
        (_("Asosiy 💼"), {"fields": ("email", "phone_number", "image")}),
        (
            _("O'zbekcha 🇺🇿"),
            {"fields": ("full_name_uz", "position_uz", "content_uz", "biography_uz", "work_date_uz")},
        ),
        (
            _("Ruscha 🇷🇺"),
            {"fields": ("full_name_ru", "position_ru", "content_ru", "biography_ru", "work_date_ru")},
        ),
        (
            _("Inglizcha 🇺🇸"),
            {"fields": ("full_name_en", "position_en", "content_en", "biography_en", "work_date_en")},
        ),
        (_("Qo'shimcha 🖋"), {"fields": ("order", "active")}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form




class WorkDescriptionInline(admin.StackedInline):
    model = models.WorkDescription
    exclude = ("work_description",)
    extra = 1


class ConditionInline(admin.StackedInline):
    model = models.Condition
    extra = 1
    exclude = ("condition",)

    


class WorkRequirementInline(admin.StackedInline):
    model = models.WorkRequirement
    extra = 1
    exclude = ("requirement",)






@admin.register(models.Representative)
class RepresentativeAdmin(ImageFieldMixin, admin.ModelAdmin):
    list_display = ("id", "short_full_name", "phone_number", "active", "created_at", "updated_at")
    search_fields = (
        "full_name",
        "position",
    )
    list_display_links = ("id", "short_full_name")
    list_filter = ("active", "country__title", "created_at", "updated_at")
    readonly_fields = ("latitude", "longitude")
    exclude = ("full_name", "position", "city", "content")
   
    fieldsets = (
        (
            _("Asosiy 💼"),
            {"fields": ("email", "country", "image", "phone_number", "location_url", "latitude", "longitude")},
        ),
        (
            _("O'zbekcha 🇺🇿"),
            {
                "fields": (
                    "full_name_uz",
                    "city_uz",
                    "slug_from_lang",
                    "slug",
                    "position_uz",
                    "content_uz",
                )
            },
        ),
        (
            _("Ruscha 🇷🇺"),
            {
                "fields": (
                    "full_name_ru",
                    "city_ru",
                    "position_ru",
                    "content_ru",
                )
            },
        ),
        (
            _("Inglizcha 🇺🇸"),
            {
                "fields": (
                    "full_name_en",
                    "city_en",
                    "position_en",
                    "content_en",
                )
            },
        ),
        (_("Qo'shimcha 🖋"), {"fields": ("active",)}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form









@admin.register(models.Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "short_title",
        "address",
        "job_type",
        "active",
        "created_at",
        "updated_at",
    )
    list_display_links = ("id", "short_title", "address")
    list_filter = ("job_type", "bool", "active", "created_at", "updated_at")
    readonly_fields = (
        "title",
        "description",
        "address",
        "content",
    )
    search_fields = (
        "title",
        "description",
        "content",
    )
    exclude = (
        "full_name",
        "position",
    )
    inlines = [WorkDescriptionInline, ConditionInline, WorkRequirementInline]
    fieldsets = (
        (
            _("Asosiy 💼"),
            {
                "fields": (
                    "bool",
                    "wage_from",
                    "wage_to",
                    "job_type",
                    "phone_number",
                )
            },
        ),
        (
            _("O'zbekcha 🇺🇿"),
            {
                "fields": (
                    "title_uz",
                    "slug_from_lang",
                    "slug",
                    "description_uz",
                    "address_uz",
                    "content_uz",
                )
            },
        ),
        (
            _("Ruscha 🇷🇺"),
            {
                "fields": (
                    "title_ru",
                    "description_ru",
                    "address_ru",
                    "content_ru",
                )
            },
        ),
        (
            _("Inglizcha 🇺🇸"),
            {
                "fields": (
                    "title_en",
                    "description_en",
                    "address_en",
                    "content_en",
                )
            },
        ),
        (_("Qo'shimcha 🖋"), {"fields": ("active",)}),
    )

    

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(models.ResumeApplication)
class ResumeApplication(admin.ModelAdmin):
    list_filter = (
        "active",
        "created_at",
    )
    list_display = ("id", "phone_number", "file", "created_at", "active")
    list_display_links = ("id", "phone_number")
    readonly_fields = ("full_name", "created_at", "phone_number", "file", "resume")
    fieldsets = ((_("Asosiy 💼"), {"fields": ("resume", "phone_number", "file", "created_at", "active")}),)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
