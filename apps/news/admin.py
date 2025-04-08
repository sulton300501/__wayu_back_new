from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.common.admin import ImageFieldMixin
from apps.news import models
from core.settings.base import MODELTRANSLATION_LANGUAGES


@admin.register(models.EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "short_name", "order", "created_at", "updated_at")
    list_display_links = ("id", "short_name")
    ordering = ("id", "order")
    list_filter = ("created_at", "updated_at")
    search_fields = ("name_uz", "name_ru", "name_en")
    exclude = ("name",)

    fieldsets = (
        (
            _("O'zbekcha 🇺🇿"),
            {
                "fields": (
                    "name_uz",
                    "slug_from_lang",
                    "slug",
                )
            },
        ),
        (_("Ruscha 🇷🇺"), {"fields": ("name_ru",)}),
        (_("Inglizcha 🇺🇸"), {"fields": ("name_en",)}),
        (
            _("Qo'shimcha 🖋"),
            {"fields": ("order",)},
        ),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form
    



class EventGalleryInline(ImageFieldMixin , admin.StackedInline):
    model = models.EventGallery
    raw_id_fields = [
        "event",
    ]
    extra = 0

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form




@admin.register(models.Event)
class EventAdmin(ImageFieldMixin, admin.ModelAdmin):
    list_display = ("id", "short_title", "category", "views_count", "active", "created_at", "updated_at")
    list_display_links = ("id", "short_title")
    search_fields = ("title_uz", "title_ru", "title_en")
    readonly_fields = ["views_count"]
    inlines = [EventGalleryInline]
    ordering = ("id", "views_count")
    list_filter = ("category", "active", "created_at", "updated_at")
    exclude = (
        "title",
        "content",
    )
    fieldsets = (
        (_("Asosiy 💼"), {"fields": ("category", "country", "image", "date", "address")}),
        (_("O'zbekcha 🇺🇿"), {"fields": ("title_uz", "slug_from_lang", "slug", "content_uz")}),
        (_("Ruscha 🇷🇺"), {"fields": ("title_ru", "content_ru")}),
        (_("Inglizcha 🇺🇸"), {"fields": ("title_en", "content_en")}),
        (
            _("Qo'shimcha 🖋"),
            {
                "fields": (
                    "views_count",
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


@admin.register(models.NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "short_name", "order", "active", "created_at", "updated_at")
    list_display_links = ("id", "short_name")
    ordering = ("id", "order")
    list_filter = ("active", "created_at", "updated_at")
    search_fields = ("name_uz", "name_ru", "name_en")
    exclude = ("name",)

    fieldsets = (
        (
            _("O'zbekcha 🇺🇿"),
            {
                "fields": (
                    "name_uz",
                    "slug_from_lang",
                    "slug",
                )
            },
        ),
        (_("Ruscha 🇷🇺"), {"fields": ("name_ru",)}),
        (_("Inglizcha 🇺🇸"), {"fields": ("name_en",)}),
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




class NewsGalleryInline(admin.StackedInline):
    model = models.NewsGallery
    raw_id_fields = [
        "news",
    ]
    extra = 0

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form






@admin.register(models.News)
class NewsAdmin(ImageFieldMixin, admin.ModelAdmin):
    list_display = ("id", "short_title", "category", "views_count", "active", "created_at", "updated_at")
    readonly_fields = ["views_count"]
    inlines = [NewsGalleryInline]
    ordering = ("-id", "views_count")
    list_display_links = ("id", "short_title")
    list_filter = ("category", "active", "created_at", "updated_at")
    search_fields = ("title_uz", "title_ru", "title_en")
    exclude = (
        "title",
        "content",
    )
    fieldsets = (
        (_("Asosiy 💼"), {"fields": ("category", "country", "image", "tags")}),
        (_("O'zbekcha 🇺🇿"), {"fields": ("title_uz", "slug_from_lang", "slug", "content_uz")}),
        (_("Ruscha 🇷🇺"), {"fields": ("title_ru", "content_ru")}),
        (_("Inglizcha 🇺🇸"), {"fields": ("title_en", "content_en")}),
        (
            _("Qo'shimcha 🖋"),
            {
                "fields": (
                    "views_count",
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





@admin.register(models.NewsTag)
class NewsTagAdmin(admin.ModelAdmin):
    list_display = ("id", "short_name")
    list_display_links = ("id", "short_name")
    ordering = ("id",)
    search_fields = ("name_uz", "name_ru", "name_en")
    fieldsets = (
        (_("O'zbekcha 🇺🇿"), {"fields": ("name_uz",)}),
        (_("Ruscha 🇷🇺"), {"fields": ("name_ru",)}),
        (_("Inglizcha 🇺🇸"), {"fields": ("name_en",)}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form
