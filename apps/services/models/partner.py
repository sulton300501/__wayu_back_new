from ckeditor_uploader.fields import RichTextUploadingField
from phonenumber_field.modelfields import PhoneNumberField
from sorl.thumbnail import ImageField

from django.conf import settings
from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.translation import gettext_lazy as _

from apps.common.helpers import get_long_lat
from apps.common.models.base import (
    ActiveModel,
    BaseModel,
    MultiLangSlugify,
    SingletonModel,
)
from apps.common.models.fields import OrderField
from apps.common.models.model import Country
from apps.common.utils import generate_upload_path


class LegalLabAbout(SingletonModel, BaseModel):
    title = models.CharField(max_length=255, verbose_name=_("sarlavha"))
    description = models.CharField(verbose_name=_("batafsil"), max_length=255)
    youtube_thumbnail = ImageField(upload_to=generate_upload_path, verbose_name=_("youtube rasmi"))
    youtube_url = models.URLField(max_length=255, verbose_name=_("youtubedan havola"))

    def __str__(self):
        return self.title

    @property
    def short_title(self):
        return truncatechars(self.title, 30)

    short_title.fget.short_description = _("sarlavha")  # type: ignore # noqa: F401

    @property
    def get_youtube_thumbnail(self):
        if self.youtube_thumbnail:
            return f"{settings.HOST}{self.youtube_thumbnail.url}"

    class Meta:
        verbose_name = _("Yuridik laboratoriya")
        verbose_name_plural = _("Yuridik laboratoriya")


class Support(ActiveModel, BaseModel):
    title = models.CharField(max_length=255, verbose_name=_("sarlavha"))
    icon = models.FileField(verbose_name=_("belgisi(.svg)"), upload_to=generate_upload_path)
    description = models.CharField(verbose_name=_("batafsil"), max_length=255)
    order = OrderField()

    def __str__(self):
        return self.title

    @property
    def get_icon(self):
        if self.icon:
            return f"{settings.HOST}{self.icon.url}"

    @property
    def short_title(self):
        return truncatechars(self.title, 30)

    short_title.fget.short_description = _("sarlavha")  # type: ignore # noqa: F401

    class Meta:
        verbose_name = _("Qo'llab-quvvatlash")
        verbose_name_plural = _("Qo'llab-quvvatlash")


class OrganizationsCategory(MultiLangSlugify, BaseModel):
    title = models.CharField(max_length=63, verbose_name=_("nomi"))
    SLUG_FROM_FIELD = "title"  # type: ignore # noqa: F401

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Tashkilot turi")
        verbose_name_plural = _("Tashkilot turlari")


class Embassy(ActiveModel, MultiLangSlugify, BaseModel):
    organization_category = models.ForeignKey(
        "OrganizationsCategory", verbose_name=_("tashkilot turi"), on_delete=models.CASCADE
    )
    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name=_("davlat"))
    full_name = models.CharField(max_length=256, verbose_name=_("F.I.SH"))
    position = models.CharField(max_length=256, verbose_name=_("Lavozimi"))
    image = ImageField(verbose_name=_("rasmi"), upload_to=generate_upload_path)
    phone_number = PhoneNumberField(verbose_name=_("telefon raqami"))
    email = models.EmailField(verbose_name=_("elektron pochtasi"))
    content = RichTextUploadingField(verbose_name=_("vazifasi"))
    location_url = models.URLField(max_length=300, verbose_name=_("joylashinuvi"))
    latitude = models.CharField(max_length=55, verbose_name=_("kenglik"), blank=True, null=True)
    longitude = models.CharField(max_length=55, verbose_name=_("uzunlik"), blank=True, null=True)
    SLUG_FROM_FIELD = "full_name"  # type: ignore

    def clean(self , *args , **kwargs):
        long_lat = get_long_lat(self.location_url)
        self.longitude = long_lat[0].get("long", None)
        self.latitude = long_lat[0].get("lat", None)
        super(Embassy , self)
        

    @property
    def get_image(self):
        if self.image:
            return f"{settings.HOST}{self.image.url}"

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _("Elchixona va konsullik ")
        verbose_name_plural = _("Elchixonalar va konsulliklar")


class PartnersCategory(MultiLangSlugify, BaseModel):
    title = models.CharField(max_length=63, verbose_name=_("nomi"))
    SLUG_FROM_FIELD = "title"  # type: ignore # noqa: F401

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Hamkorlik turi")
        verbose_name_plural = _("Hamkorlik turlari")


class Partnership(BaseModel):
    partner_category = models.ForeignKey("PartnersCategory", on_delete=models.CASCADE, verbose_name=_("hamkorlik turi"))
    description = RichTextUploadingField(verbose_name=_("basafsil"))

    def __str__(self):
        return self.description

    @property
    def short_description(self):
        return truncatechars(self.description, 30)

    short_description.fget.short_description = _("basafsil")  # type: ignore # noqa: F401

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Hamkorlik ")
        verbose_name_plural = _("Hamkorliklar")


class PartnerOrganization(ActiveModel, BaseModel):
    partner_category = models.ForeignKey(
        "PartnersCategory", verbose_name=_("hamkorlik turi"), on_delete=models.CASCADE, null=True, blank=True
    )
    title = models.CharField(_("tashkilot nomi"), max_length=256)
    logo = models.FileField(_("logotip(.svg)"), upload_to=generate_upload_path)
    site_name = models.URLField(verbose_name=_("sayt nomi"))
    order = OrderField()

    def __str__(self) -> str:
        return f"{self.title}"

    @property
    def get_logo(self):
        if self.logo:
            return f"{settings.HOST}{self.logo.url}"

    @property
    def short_title(self):
        return truncatechars(self.title, 30)

    short_title.fget.short_description = _("sarlavha")  # type: ignore # noqa: F401

    class Meta:
        ordering = ("order",)
        verbose_name = _("Hamkor tashkilot ")
        verbose_name_plural = _("Hamkor tashkilotlar")
