from django.db import models
from apps.common.models.fields import OrderField
from apps.common.models.base import *
from django.template.defaultfilters import  truncatechars
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from sorl.thumbnail import ImageField
from apps.common.models.model import Country
from apps.common.utils import generate_upload_path

# Create your models here.


class EventCategory(MultiLangSlugify , BaseModel):
    name = models.CharField(max_length=255 , verbose_name=_("nomi"))
    order = OrderField()
    SLUG_FROM_FIELD = "name"


    @property
    def short_name(self):
        return truncatechars(self.name , 30)
    
    short_name.fget.short_description = _("nomi")

    class Meta:
        ordering = ("order",)
        verbose_name = _("Tadbir kategoriyasi ")
        verbose_name_plural = _("1.Tadbirlar kategoriyalari ")

    def __str__(self):
        return self.name



class Event(BaseModel , ActiveModel , MultiLangSlugify):
    category = models.ForeignKey("EventCategory", on_delete=models.PROTECT, verbose_name=_("kategoriyasi"))
    title = models.CharField(max_length=512, verbose_name=_("sarlavha"))
    content = RichTextUploadingField(_("matn"))
    image = ImageField(verbose_name=_("Rasm"), upload_to=generate_upload_path)
    address = models.CharField(_("address"), max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name=_("davlat"))
    views_count = models.PositiveBigIntegerField(_("ko'rganlar soni"), default=0)
    date = models.DateTimeField(_("tadbir kuni"))
    SLUG_FROM_FIELD = "title"  # type: ignore # noqa: F401

    @property
    def get_image(self):
        if self.image:
            return f"{settings.HOST}{self.image.url}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Tadbir ")
        verbose_name_plural = _("2.Tadbirlar ")

    @property
    def short_title(self):
        return truncatechars(self.title, 30)

    short_title.fget.short_description = _("sarlavha")  # type: ignore # noqa: F401

    def __str__(self):
        return self.title
    


class EventGallery(BaseModel):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name=_("tadbir"))
    image = ImageField(verbose_name=_("rasm"), upload_to=generate_upload_path)

    def __str__(self):
        return self.event.title

    class Meta:
        verbose_name = _("Tadbir galareyasi")
        verbose_name_plural = _("Tadbirlar Galareyalari")







class NewsCategory(ActiveModel, MultiLangSlugify, BaseModel):
    name = models.CharField(max_length=256, verbose_name=_("nomi"))
    order = OrderField()
    SLUG_FROM_FIELD = "name"  # type: ignore # noqa: F401

    @property
    def short_name(self):
        return truncatechars(self.name, 30)

    short_name.fget.short_description = _("nomi")  # type: ignore # noqa: F401

    class Meta:
        ordering = ("order",)
        verbose_name = _("Yangiliklar kategoriyasi ")
        verbose_name_plural = _("3.Yangiliklar kategoriyalari ")

    def __str__(self):
        return self.name
    




class NewsTag(BaseModel):
    name = models.CharField(max_length=512, verbose_name=_("nomi"))

    class Meta:
        verbose_name = _("Yangiliklar tegi ")
        verbose_name_plural = _("4.Yangiliklar teglari")

    def __str__(self):
        return self.name

    @property
    def short_name(self):
        return truncatechars(self.name, 30)

    short_name.fget.short_description = _("nomi")  # type: ignore # noqa: F401



class News(ActiveModel , MultiLangSlugify , BaseModel):
    image = ImageField(verbose_name=_("rasm"), upload_to=generate_upload_path)
    title = models.CharField(max_length=256, verbose_name=_("sarlavha"))
    content = RichTextUploadingField(verbose_name=_("batafsil"))
    views_count = models.PositiveBigIntegerField(verbose_name=_("ko'rganlar soni"), default=0)
    category = models.ForeignKey(
        "NewsCategory",
        on_delete=models.PROTECT,
        verbose_name=_("kategoriyasi"),
    )
    tags = models.ManyToManyField("NewsTag" , verbose_name=_("teglar"))
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name=_("davlat"))
    SLUG_FROM_FIELD = "title"  # type: ignore # noqa: F401

    @property
    def get_image(self):
        if self.image:
            return f"{settings.HOST}{self.image.url}"

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Yangilik ")
        verbose_name_plural = _("5.Yangiliklar ")

    @property
    def short_title(self):
        return truncatechars(self.title, 30)

    short_title.fget.short_description = _("sarlavha")  # type: ignore # noqa: F401

    def __str__(self):
        return self.title
    



class NewsGallery(BaseModel):
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name=_("yangilik"))
    image = ImageField(verbose_name=_("rasm"), upload_to=generate_upload_path)

    def __str__(self):
        return self.news.title

    class Meta:
        verbose_name = _("Yangilik galareyasi")
        verbose_name_plural = _("Yangiliklar Galareyalari")
