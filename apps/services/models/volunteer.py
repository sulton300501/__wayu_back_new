from ckeditor_uploader.fields import RichTextUploadingField
from phonenumber_field.modelfields import PhoneNumberField
from sorl.thumbnail import ImageField

from django.conf import settings
from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.translation import gettext_lazy as _

from apps.common.models.base import ActiveModel, BaseModel, SingletonModel
from apps.common.models.fields import OrderField
from apps.common.models.model import Country
from apps.common.utils import generate_upload_path


class ForVolunteer(SingletonModel, BaseModel):
    title = models.CharField(max_length=255, verbose_name=_("sarlavhasi"))
    content = RichTextUploadingField(verbose_name=_("batafsil"))

    def __str__(self):
        return self.title

    @property
    def short_title(self):
        return truncatechars(self.title, 30)

    short_title.fget.short_description = _("sarlavha")  # type: ignore # noqa: F401

    class Meta:
        verbose_name = _("Ko'ngillilar uchun ")
        verbose_name_plural = _("Ko'ngillilar uchun")


class VolunteerResume(BaseModel):
    full_name = models.CharField(max_length=256, verbose_name=_("F.I.SH"))
    phone_number = models.CharField(verbose_name=_("Telefon Raqam"), max_length=20)
    email = models.EmailField(verbose_name=_("elektron pochta"))
    file = models.FileField(verbose_name=_("joylangan rezyume"), upload_to=generate_upload_path)
    active = models.BooleanField(default=False, verbose_name=_("rezyume ko'rilganmi ?"))

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Volontyor bo'lish uchun ariza ")
        verbose_name_plural = _("Volontyor bo'lish uchun arizalar")

    def __str__(self):
        return self.phone_number


class Volunteer(ActiveModel, BaseModel):
    full_name = models.CharField(max_length=256, verbose_name=_("F.I.SH"))
    position = models.CharField(max_length=256, verbose_name=_("lavozimi"))
    image = ImageField(upload_to=generate_upload_path, verbose_name=_("rasmi"), null=True, blank=True)
    email = models.EmailField(verbose_name=_("elektron pochta"))
    phone_number = PhoneNumberField(verbose_name=_("telefon raqami"))
    order = OrderField()

    @property
    def short_title(self):
        return truncatechars(self.full_name, 30)

    short_title.fget.short_description = _("F.I.SH")  # type: ignore # noqa: F401

    def __str__(self):
        return self.full_name

    @property
    def get_image(self):
        if self.image:
            return f"{settings.HOST}{self.image.url}"

    class Meta:
        ordering = ("order",)
        verbose_name = _("Volontyor ")
        verbose_name_plural = _("Volontyorlar")


class Coordinator(ActiveModel, BaseModel):
    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name=_("davlat"))
    full_name = models.CharField(max_length=256, verbose_name=_("F.I.SH"))
    position = models.CharField(max_length=256, verbose_name=_("lavozimi"))
    image = ImageField(upload_to=generate_upload_path, verbose_name=_("rasmi"), null=True, blank=True)
    email = models.EmailField(verbose_name=_("elektron pochta"))
    phone_number = PhoneNumberField(verbose_name=_("telefon raqami"))
    order = OrderField()

    @property
    def short_title(self):
        return truncatechars(self.full_name, 30)

    short_title.fget.short_description = _("F.I.SH")  # type: ignore # noqa: F401

    def __str__(self):
        return self.full_name

    @property
    def get_image(self):
        if self.image:
            return f"{settings.HOST}{self.image.url}"

    class Meta:
        ordering = ("order",)
        verbose_name = _("Koordinator ")
        verbose_name_plural = _("Koordinatorlar")


class Opportunity(ActiveModel, BaseModel):
    title = models.CharField(max_length=255, verbose_name=_("nomi"))
    icon = models.FileField(upload_to=generate_upload_path, verbose_name=_("belgisi(.svg)"))
    order = OrderField()

    def __str__(self):
        return self.title

    @property
    def get_icon(self):
        if self.icon:
            return f"{settings.HOST}{self.icon.url}"

    class Meta:
        ordering = ("order",)
        verbose_name = _("Imkoniyat ")
        verbose_name_plural = _("Imkoniyatlar")
