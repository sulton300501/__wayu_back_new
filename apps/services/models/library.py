from sorl.thumbnail import ImageField

from django.conf import settings
from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.translation import gettext_lazy as _

from apps.common.models.base import ActiveModel, BaseModel, MultiLangSlugify
from apps.common.models.fields import OrderField
from apps.common.utils import generate_upload_path


class LibraryCatalog(ActiveModel, MultiLangSlugify, BaseModel):
    title = models.CharField(max_length=256, verbose_name=_("katalog"), unique=True)
    order = OrderField()
    SLUG_FROM_FIELD = "title"  # type: ignore # noqa: F401

    def __str__(self):
        return self.title

    @property
    def short_title(self):
        return truncatechars(self.title, 30)

    short_title.fget.short_description = _("katalog")  # type: ignore # noqa: F401

    class Meta:
        ordering = ("order",)
        verbose_name = _("katalog ")
        verbose_name_plural = _("kataloglar")


class Book(ActiveModel, MultiLangSlugify, BaseModel):
    catalog = models.ForeignKey(LibraryCatalog, on_delete=models.CASCADE, verbose_name=_("katalog"))
    image = ImageField(upload_to=generate_upload_path, verbose_name=_("kitob rasmi"))
    name = models.CharField(max_length=255, verbose_name=_("kitob nomi"))
    author = models.CharField(max_length=255, verbose_name=_("avtori"))
    language = models.CharField(max_length=63, verbose_name=_("tili"))
    year = models.PositiveIntegerField(verbose_name=_("chop etilgan yili"), default=2000)
    page_count = models.PositiveIntegerField(verbose_name=_("varaqalari soni"))
    file = models.FileField(verbose_name=_("fayl"), upload_to=generate_upload_path)
    description = models.TextField(verbose_name=_("tavsifi"))
    order = OrderField()
    SLUG_FROM_FIELD = "name"  # type: ignore # noqa: F401

    @property
    def short_name(self):
        return truncatechars(self.name, 30)

    short_name.fget.short_description = _("kitob nomi")  # type: ignore # noqa: F401

    @property
    def get_image(self):
        if self.image:
            return f"{settings.HOST}{self.image.url}"

    @property
    def get_file(self):
        if self.file:
            return f"{settings.HOST}{self.file.url}"

    class Meta:
        ordering = ("order",)
        verbose_name = _("Kitob ")
        verbose_name_plural = _("Kitoblar")
