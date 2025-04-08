from django.contrib import admin
from apps.common.models.model import *
from core.settings.base import MODELTRANSLATION_LANGUAGES
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from django.utils.translation import gettext_lazy as _
from image_uploader_widget.widgets import ImageUploaderWidget
# Register your models here.



class ImageFieldMixin:
    formfield_overrides = {
        ImageField: {'widget': ImageUploaderWidget}
    }


class SingletonAdminMixin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.all_objects().count() > 0:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        return self.model.objects.all_objects()





@admin.register(FAQTag)
class FAQTagAdmin(admin.ModelAdmin):
    model = FAQTag
    list_display = ("id", "title")
    search_fields = ("title_uz", "title_ru", "title_en")
    ordering = ("id",)
    list_display_links = ("id", "title")
    exclude = ("title",)
    fieldsets = (
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






@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("id", "short_question", "short_answer", "order", "active", "created_at", "updated_at") 
    ordering = ("id","order")
    list_display_links = ("id", "short_question")
    list_filter = ("active", "created_at", "updated_at")
    search_fields = ("question_uz", "question_ru", "question_en")
    exclude = ("question", "answer")
    fieldsets = (
        (_("Asosiy 💼"), {"fields": ("tags",)}),
        (_("O'zbekcha 🇺🇿"), {"fields": ("question_uz", "answer_uz")}),
        (_("Ruscha 🇷🇺"), {"fields": ("question_ru", "answer_ru")}),
        (_("Inglizcha 🇺🇸"), {"fields": ("question_en", "answer_en")}),
        (
            _("Qo'shimcha 🖋"),
            {
                "fields": (
                    "active",
                    "order",
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
    




@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    list_display = (
        "id",
        "full_name",
        "phone_number",
        "created_at",
    )
    list_filter = ("created_at",)
    list_display_links = ("id", "full_name")
    readonly_fields = ("full_name", "phone_number", "question")
    ordering = ("id",)
    search_fields = (
        "full_name",
        "phone_number",
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(Contact)
class ContactAdmin(SingletonAdminMixin, admin.ModelAdmin, DynamicArrayMixin):
    list_display = (
        "main_phone_number",
        "short_title",
        "created_at",
        "updated_at",
    )
    list_display_links = ("short_title", "main_phone_number")
    exclude = (
        "title",
        "address",
    )
    fieldsets = (
        (
            _("aloqa uchun"),
            {
                "fields": (
                    "main_phone_number",
                    "emails",
                    "phones",
                )
            },
        ),
        (
            _("O'zbekcha 🇺🇿"),
            {
                "fields": (
                    "title_uz",
                    "address_uz",
                )
            },
        ),
        (
            _("Ruscha 🇷🇺"),
            {
                "fields": (
                    "title_ru",
                    "address_ru",
                )
            },
        ),
        (
            _("Inglizcha 🇺🇸"),
            {
                "fields": (
                    "title_en",
                    "address_en",
                )
            },
        ),
        (_("ijtimoiy tarmoqlar"), {"fields": ("whatsapp", "youtube", "instagram", "telegram", "twitter")}),
        (
            _("lokatsiya"),
            {
                "fields": (
                    "location",
                    "latitude",
                    "longitude",
                )
            },
        ),
    )
    readonly_fields = ("latitude", "longitude")

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    list_display = (
        "id",
        "full_name",
        "phone_number",
        "email",
        "created_at",
    )
    list_filter = ("created_at", "updated_at")
    list_display_links = ("id", "full_name")
    readonly_fields = ("full_name", "phone_number", "message", "email")
    ordering = ("id",)
    search_fields = (
        "full_name",
        "phone_number",
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(ContactUser)
class ContactUserAdmin(ImageFieldMixin, SingletonAdminMixin, admin.ModelAdmin):
    list_display = (
        "id",
        "full_name",
        "phone_number",
        "email",
        "created_at",
        "updated_at",
    )
    list_display_links = ("id", "full_name")
    exclude = ("full_name", "position", "reception_days", "description")
    fieldsets = (
        (_("Asosiy 💼"), {"fields": ("image", "phone_number", "email")}),
        (_("O'zbekcha 🇺🇿"), {"fields": ("full_name_uz", "position_uz", "reception_days_uz", "description_uz")}),
        (_("Ruscha 🇷🇺"), {"fields": ("full_name_ru", "position_ru", "reception_days_ru", "description_ru")}),
        (_("Inglizcha 🇺🇸"), {"fields": ("full_name_en", "position_en", "reception_days_en", "description_en")}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(Country)
class CountryAdmin(ImageFieldMixin, admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at", "active")
    list_display_links = (
        "id",
        "title",
    )
    search_fields = ("title",)
    list_filter = ("active",)
    exclude = ("title",)
    fieldsets = (
        (_("Asosiy 💼"), {"fields": ("flag",)}),
        (
            _("O'zbekcha 🇺🇿"),
            {"fields": ("title_uz",)},
        ),
        (
            _("Ruscha 🇷🇺"),
            {"fields": ("title_ru",)},
        ),
        (
            _("Inglizcha 🇺🇸"),
            {"fields": ("title_en",)},
        ),
        (_("Qo'shimcha 🖋"), {"fields": ("active",)}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "short_title",
        "active",
        "created_at",
        "updated_at",
    )
    list_display_links = ("id", "short_title")
    search_fields = ("title_uz", "title_ru", "title_en")
    list_filter = ("active", "created_at", "updated_at")
    exclude = ("title", "content")
    fieldsets = (
        (_("O'zbekcha 🇺🇿"), {"fields": ("title_uz", "slug_from_lang", "slug", "content_uz", 'active')}),
        (_("Ruscha 🇷🇺"), {"fields": ("title_ru", "content_ru")}),
        (_("Inglizcha 🇺🇸"), {"fields": ("title_en", "content_en")}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


