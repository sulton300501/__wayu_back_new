from apps.common.models.base import (
    ActiveModel,
    BaseModel,
    SingletonModel,
)
from django.db import models
from apps.common.models.fields import OrderField
from apps.common.models.model import Country
from apps.common.utils import generate_upload_path
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import truncatechars
from django.conf import settings


class MigrationLaw(ActiveModel, BaseModel):
    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name=_("davlat"))
    file = models.FileField(upload_to=generate_upload_path, verbose_name=_("hujjat"))
    order = OrderField()

    @property
    def get_file(self):
        if self.file:
            return f"{settings.HOST}{self.file.url}"

    class Meta:
        ordering = ("order",)
        verbose_name = _("Migratsiya qonuni ")
        verbose_name_plural = _("Migratsiya qonunlari")


class Insurance(ActiveModel, BaseModel):
    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name=_("davlat"))
    file = models.FileField(upload_to=generate_upload_path, verbose_name=_("hujjat"))
    order = OrderField()

    @property
    def get_file(self):
        if self.file:
            return f"{settings.HOST}{self.file.url}"

    class Meta:
        ordering = ("order",)
        verbose_name = _("Sug'urta ")
        verbose_name_plural = _("Sug'urtalar")


class CountryLaw(ActiveModel, BaseModel):
    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name=_("davlat"))
    description = models.TextField(verbose_name=_("batafsil"))
    views_count = models.PositiveIntegerField(verbose_name=_("ko'rishlar soni"), default=0)
    order = OrderField()

    def __str__(self):
        return self.description

    @property
    def short_description(self):
        return truncatechars(self.description, 60)

    short_description.fget.short_description = _("batafsil")  # type: ignore # noqa: F401

    class Meta:
        ordering = ("order",)
        verbose_name = _("Davlat qonuni ")
        verbose_name_plural = _("Davlat qonunlari")


class Obligations(SingletonModel, BaseModel):
    title = models.CharField(max_length=256, verbose_name=_("sarlavhasi"))
    content = RichTextUploadingField(verbose_name=_("batafsil"))
    views_count = models.PositiveIntegerField(default=0, verbose_name=_("korishlar soni"))

    @property
    def short_title(self):
        return truncatechars(self.title, 30)

    short_title.fget.short_description = _("sarlavhasi")  # type: ignore # noqa: F401

    class Meta:
        verbose_name = _("Huquqlar va majburiyatlar ")
        verbose_name_plural = _("Huquqlar va majburiyatlar")
