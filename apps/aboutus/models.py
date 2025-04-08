import datetime

from ckeditor_uploader.fields import RichTextUploadingField
from phonenumber_field.modelfields import PhoneNumberField
from sorl.thumbnail import ImageField

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
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
from apps.common.utils import generate_upload_path


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Header(SingletonModel, BaseModel):
    banner = ImageField(upload_to=generate_upload_path, verbose_name=_("banner rasmi"))
    icon = models.FileField(
        upload_to=generate_upload_path,
        verbose_name=_("belgisi(.svg)"),
    )
    title = models.CharField(max_length=256, verbose_name=_("sarlavha"))
    description = models.CharField(max_length=1024, verbose_name=_("tavsif"))

    def __str__(self):
        return self.title

    @property
    def get_banner(self):
        if self.banner:
            return f"{settings.HOST}{self.banner.url}"

    @property
    def get_icon(self):
        if self.icon:
            return f"{settings.HOST}{self.icon.url}"

    @property
    def short_title(self):
        return truncatechars(self.title, 30)

    short_title.fget.short_description = _("sarlavha")  # type: ignore # noqa: F401

    class Meta:
        verbose_name = _("Bosh sahifa ")
        verbose_name_plural = _("1. Bosh sahifa")


class WhatWeDo(SingletonModel, BaseModel):
    title = models.CharField(max_length=255, verbose_name=_("sarlavha"))
    content = RichTextUploadingField(verbose_name=_("batafsil"))
    short_title = models.CharField(max_length=255, verbose_name=_("qisqa sarlavha"))
    short_text = models.TextField(max_length=255, verbose_name=_("qisqa matn"))
    youtube_thumbnail = ImageField(upload_to=generate_upload_path, verbose_name=_("youtube rasmi"))
    youtube_url = models.URLField(max_length=255, verbose_name=_("youtubedan havola"))
    views_count = models.PositiveBigIntegerField(verbose_name=_("ko'rganlar soni"), default=0)
    status_statistic = models.CharField(_("Statistika holati"), max_length=256)

    @property
    def short_title_func(self):
        return truncatechars(self.short_title, 30)

    short_title_func.fget.short_description = _("qisqacha sarlavha")  # type: ignore # noqa: F401

    @property
    def get_youtube_thumbnail(self):
        if self.youtube_thumbnail:
            return f"{settings.HOST}{self.youtube_thumbnail.url}"

    def __str__(self):
        return self.short_title

    class Meta:
        verbose_name = _("Siz bilishingiz kerak ")
        verbose_name_plural = _("2. Siz bilishingiz kerak")


class AboutCenterHistory(ActiveModel, BaseModel):
    title = models.CharField(max_length=64, verbose_name=_("F.I.SH"))
    position = models.CharField(max_length=256, verbose_name=_("lavozimi"))
    image = ImageField(upload_to=generate_upload_path, verbose_name=_("rasmi"))
    address = models.CharField(max_length=255, verbose_name=_("Manzil"))
    phone_number = PhoneNumberField(verbose_name=_("telefon raqami"), null=True)
    description = models.TextField(max_length=512, verbose_name=_("batafsil"))
    year = models.IntegerField(_("yil"), validators=[MinValueValidator(2000), max_value_current_year])

    @property
    def short_title(self):
        return truncatechars(self.title, 30)

    short_title.fget.short_description = _("F.I.SH")  # type: ignore # noqa: F401

    def __str__(self):
        return f"{self.title} - {self.year}"

    @property
    def get_image(self):
        if self.image:
            return f"{settings.HOST}{self.image.url}"

    class Meta:
        ordering = ("year",)
        verbose_name = _("Markaz tarixi ")
        verbose_name_plural = _("3. Markaz tarixi")


class AboutCenterGoal(ActiveModel, BaseModel):
    description = models.TextField(max_length=512, verbose_name=_("matn"))
    order = OrderField()

    @property
    def short_title(self):
        return truncatechars(self.description, 30)

    short_title.fget.short_description = _("batafsil")  # type: ignore # noqa: F401

    def __str__(self):
        return f"Vazifalar ({self.order})"

    class Meta:
        ordering = ("order",)
        verbose_name = _("Markaz vazifasi ")
        verbose_name_plural = _("4. Markaz vazifalari")


class Statistic(ActiveModel, BaseModel):
    icon = models.FileField(verbose_name=_("ikonka"), upload_to=generate_upload_path)
    description = models.TextField(verbose_name=_("matn"))
    number = models.IntegerField(verbose_name=_("sonlar"))
    order = OrderField()

    @property
    def get_icon(self):
        if self.icon:
            return f"{settings.HOST}{self.icon.url}"

    @property
    def short_title(self):
        return truncatechars(self.description, 30)

    short_title.fget.short_description = _("sarlavha")  # type: ignore # noqa: F401

    def __str__(self):
        return str(self.number)

    class Meta:
        ordering = ("order",)
        verbose_name = _("Statistika")
        verbose_name_plural = _("5. Statistika")


class Management(ActiveModel, BaseModel):
    full_name = models.CharField(max_length=256, verbose_name=_("F.I.SH"))
    position = models.CharField(max_length=256, verbose_name=_("lavozimi"))
    image = ImageField(upload_to=generate_upload_path, verbose_name=_("rasmi"))
    email = models.EmailField(verbose_name=_("elektron pochta"))
    phone_number = PhoneNumberField(verbose_name=_("telefon raqami"))
    work_date = models.CharField(max_length=256, verbose_name=_("ish kunlari"))
    content = RichTextUploadingField(verbose_name=_("vazifalari"), null=True, blank=True)
    biography = RichTextUploadingField(verbose_name=_("biografiyasi"), null=True, blank=True)
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
        verbose_name = _("Markaz rahbariyati ")
        verbose_name_plural = _("6. Markaz rahbariyati")


class JobType(models.TextChoices):
    quarter_time = "quarter_time", _("0,25 ish stavkasi")
    part_time = "part_time", _("0,5 ish stavkasi")
    full_time = "full_time", _("to'liq ish stavkasi")


class Representative(ActiveModel, MultiLangSlugify, BaseModel):
    full_name = models.CharField(max_length=255, verbose_name=_("F.I.SH"))
    country = models.ForeignKey("common.Country", on_delete=models.CASCADE, verbose_name=_("davlat"))
    image = ImageField(upload_to=generate_upload_path, verbose_name=_("rasmi"))
    city = models.CharField(max_length=127, verbose_name=_("joylashgan shahari"))
    position = models.CharField(max_length=255, verbose_name=_("ish"))
    phone_number = PhoneNumberField(verbose_name=_("telefon raqami"))
    email = models.EmailField(max_length=255, verbose_name=_("email pochta"))
    content = RichTextUploadingField(verbose_name=_("vazifasi"))
    location_url = models.URLField(max_length=300, verbose_name=_("joylashinuvi"))
    latitude = models.CharField(max_length=55, verbose_name=_("kenglik"), blank=True, null=True)
    longitude = models.CharField(max_length=55, verbose_name=_("uzunlik"), blank=True, null=True)
    SLUG_FROM_FIELD = "full_name"  # type: ignore # noqa: F401

    def clean(self, *args, **kwargs):
        long_lat = get_long_lat(self.location_url)
        self.longitude = long_lat[0].get("long", None)
        self.latitude = long_lat[0].get("lat", None)
        super(Representative, self).clean(*args , **kwargs)

    @property
    def get_image(self):
        if self.image:
            return f"{settings.HOST}{self.image.url}"

    @property
    def short_full_name(self):
        return truncatechars(self.full_name, 30)

    @property
    def short_position(self):
        return truncatechars(self.position, 30)

    short_full_name.fget.short_description = _("f.i.sh")  # type: ignore # noqa: F401

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _("Vakil")
        verbose_name_plural = _("7. Vakillar")


class WorkDescription(BaseModel):
    work_description = models.CharField(max_length=512, verbose_name=_("ish tavsifi"))
    resume = models.ForeignKey(
        "Vacancy", on_delete=models.CASCADE, verbose_name=_("vakansiya"), related_name="workdescription"
    )

    def __str__(self):
        return self.work_description

    class Meta:
        verbose_name = _("Ish tavsiloti ")
        verbose_name_plural = _("Ish tavsilotlari")


class Condition(BaseModel):
    condition = models.CharField(max_length=512, verbose_name=_("mehnat va ish haqi shartlari"))
    resume = models.ForeignKey(
        "Vacancy", on_delete=models.CASCADE, verbose_name=_("vakansiya"), related_name="workcondition"
    )

    def __str__(self):
        return self.condition

    class Meta:
        verbose_name = _("Mehnat va ish haqi sharti ")
        verbose_name_plural = _("Mehnat va ish haqi shartlari")


class WorkRequirement(BaseModel):
    requirement = models.CharField(max_length=512, verbose_name=_("talablar"))
    resume = models.ForeignKey(
        "Vacancy", on_delete=models.CASCADE, verbose_name=_("vakansiya"), related_name="workrequirement"
    )

    def __str__(self):
        return self.requirement

    class Meta:
        verbose_name = _("Talab ")
        verbose_name_plural = _("Talablar")


class Vacancy(ActiveModel, MultiLangSlugify, BaseModel):
    title = models.CharField(max_length=255, verbose_name=_("Sarlavha"))
    description = models.TextField(max_length=1000, verbose_name=_("Tavsifi"))
    address = models.CharField(max_length=255, verbose_name=_("Manzil"))
    bool = models.BooleanField(verbose_name=_("suhbat asosida"), default=False)
    wage_from = models.IntegerField(verbose_name=_("Maosh dan"), default=0)
    wage_to = models.IntegerField(verbose_name=_("Maosh gacha"), default=0)
    job_type = models.CharField(max_length=55, verbose_name=_("ish stavkasi"), choices=JobType.choices)
    content = RichTextUploadingField(verbose_name=_("batafsil"))
    view_count = models.PositiveBigIntegerField(verbose_name=_("Ko'rilgan soni"), default=0)
    phone_number = PhoneNumberField(verbose_name=_("telefon raqami"))
    SLUG_FROM_FIELD = "title"  # type: ignore # noqa: F401

    class Meta:
        verbose_name = _("Vakansiya ")
        verbose_name_plural = _("8. Vakansiyalar")

    @property
    def short_title(self):
        return truncatechars(self.title, 30)

    short_title.fget.short_description = _("sarlavha")  # type: ignore # noqa: F401

    def __str__(self):
        return self.title


class ResumeApplication(BaseModel):
    resume = models.ForeignKey("Vacancy", on_delete=models.CASCADE, verbose_name=_("Vakansiya"), null=True, blank=True)
    full_name = models.CharField(max_length=256, verbose_name=_("F.I.SH"), null=True, blank=True)
    phone_number = models.CharField(verbose_name=_("Telefon Raqam"), max_length=20)
    file = models.FileField(verbose_name=_("joylangan rezyume"), upload_to=generate_upload_path)
    active = models.BooleanField(default=False, verbose_name=_("rezyume ko'rilganmi ?"))

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Ishga kirish uchun Ariza ")
        verbose_name_plural = _("9. Ishga kirish uchun Arizalar")

    def __str__(self):
        return self.phone_number
    
