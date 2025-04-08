from ckeditor_uploader.fields import RichTextUploadingField
from sorl.thumbnail import ImageField

from django.conf import settings
from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.translation import gettext_lazy as _

from apps.common.models.base import ActiveModel, BaseModel, SingletonModel
from apps.common.models.fields import OrderField
from apps.common.utils import generate_upload_path





class ServiceCategory(BaseModel):
    title = models.CharField(max_length=256, verbose_name=_("kategoriya nomi"), unique=True)
    icon = models.FileField(verbose_name=_("belgisi(.svg)"), upload_to=generate_upload_path)
    order = OrderField()
    path = models.CharField(max_length=256, verbose_name=_("PATH"))

    def __str__(self):
        return f"{self.title}"

    @property
    def short_title(self):
        return truncatechars(self.title, 30)

    short_title.fget.short_description = _("kategoriya nomi")  # type: ignore # noqa: F401

    class Meta:
        ordering = ("order",)
        verbose_name = _("Xizmat kategoriya ")
        verbose_name_plural = _("1. Xizmat kategoriyalari")

    @property
    def get_icon(self):
        if self.icon:
            return f"{settings.HOST}{self.icon.url}"
        



class CareerAbout(SingletonModel, BaseModel):
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
        verbose_name = _("Karyera")
        verbose_name_plural = _("Karyera")





class YoungInnovator(ActiveModel, BaseModel):
    title = models.CharField(max_length=256, verbose_name=_("turi"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Yosh innovator ")
        verbose_name_plural = _("Yosh innovator")


class PhotoGallery(ActiveModel, BaseModel):
    image = ImageField(upload_to=generate_upload_path, verbose_name=_("rasmi"))

    @property
    def get_image(self):
        if self.image:
            return f"{settings.HOST}{self.image.url}"

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Fotogalereya ")
        verbose_name_plural = _("Fotogalereyalar")


class PhotoGalleryCompatriots(ActiveModel, BaseModel):
    image = ImageField(upload_to=generate_upload_path, verbose_name=_("rasmi"))

    @property
    def get_image(self):
        if self.image:
            return f"{settings.HOST}{self.image.url}"

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Yosh vatandoshlar fotogalereyasi ")
        verbose_name_plural = _("Yosh vatandoshlar fotogalereyalari")


class GratuitousHelp(SingletonModel, BaseModel):
    description = models.TextField(verbose_name=_("batafsil"))

    def __str__(self):
        return self.description

    @property
    def short_description(self):
        return truncatechars(self.description, 30)

    short_description.fget.short_description = _("basafsil")  # type: ignore # noqa: F401

    class Meta:
        verbose_name = _("Bepul yordam")
        verbose_name_plural = _("Bepul yordam")


class YoungCompatriots(SingletonModel, BaseModel):
    title = models.CharField(max_length=256, verbose_name=_("nomi"))
    content = RichTextUploadingField(verbose_name=_("batafsil"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Yosh vatandoshlar ")
        verbose_name_plural = _("Yosh vatandoshlar")





class GoogleForm(SingletonModel, BaseModel):
    google_form = models.CharField(max_length=1023, verbose_name=_("Google forma"))

    def __str__(self):
        return self.google_form

    class Meta:
        verbose_name = _("Google forma")
        verbose_name_plural = _("Google forma")


