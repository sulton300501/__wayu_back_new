from django.db import models
from apps.common.models.base import *
from django.utils.translation import gettext_lazy as _
from sorl.thumbnail import ImageField
from apps.common.utils import generate_upload_path
from django.conf import settings
from django.template.defaultfilters import truncatechars
from apps.common.models.fields import OrderField
from mptt.models import MPTTModel , TreeForeignKey


# Create your models here.







class Slider(SingletonModel , BaseModel):
    title = models.CharField(_("sarlavhasi"), max_length=512)
    description = models.CharField(verbose_name=_("tavsifi"),max_length=512)
    image = ImageField(_("slider rasmi") , upload_to=generate_upload_path)

    def __str__(self):
        return f"{self.title}"
    
    
    @property
    def get_image(self):
        if self.image:
            return f"{settings.HOST}{self.image.url}"
    
    @property
    def short_title(self):
        return truncatechars(self.title , 30)
    
    short_title.fget.short_description = _("sarlavhasi") # type: ignore # noqa: F401

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "1. Slider"


class PayStatistic(ActiveModel , BaseModel):
    title = models.CharField(_("sarlavhasi"), max_length=512)
    icon = models.FileField(verbose_name=_("belgisi(.svg)") , upload_to=generate_upload_path)
    count = models.PositiveBigIntegerField(verbose_name=_("statistika qiymati"),default=0)
    order = OrderField()  # tartibi yani joylashuv joyi

    def __str__(self):
        return f"{self.title}"
    
    @property
    def get_icon(self):
        if self.icon:
            return f"{settings.HOST}{self.icon.url}"
    
    @property
    def short_title(self):
        return truncatechars(self.short_title , 30)
    
    short_title.fget.short_description = _("sarlavha")

    class Meta:
        ordering = ("order",)
        verbose_name = _("Xayriya statistikasi ")
        verbose_name_plural = _("2. Xayriya statistikasi")





class BannerMenu(ActiveModel, BaseModel):
    title = models.CharField(max_length=31, verbose_name=_("Menyu nomi"), unique=True)
    short_description = models.CharField(max_length=63, verbose_name=_("Menu haqida qisqacha"))
    icon = models.FileField(verbose_name=_("belgisi(.svg)"), upload_to=generate_upload_path, null=True, blank=True)
    order = OrderField()
    path = models.CharField(max_length=256, verbose_name=_("PATH"))

    def __str__(self):
        return f"{self.title}"

    @property
    def get_icon(self):
        if self.icon:
            return f"{settings.HOST}{self.icon.url}"

    @property
    def short_title(self):
        return truncatechars(self.title, 30)

    short_title.fget.short_description = _("Menyu nomi")  # type: ignore # noqa: F401

    class Meta:
        ordering = ("order",)
        verbose_name = _("Banner Menyu ")
        verbose_name_plural = _("3. Banner Menyu")




class HeaderMenu(MPTTModel):
    title = models.CharField(max_length=255 , verbose_name=_("Menyu nomi") , unique=True)
    parent = TreeForeignKey("self",on_delete=models.CASCADE , null=True , blank=True , related_name="children" , verbose_name=_("yuqori menyu"))
    

    order = OrderField()
    path = models.CharField(max_length=256 , verbose_name=_("PATH"))


    class MPTTModel:
        order_insertion_by = ["title"]

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        ordering = ("order",)
        verbose_name = _("Header Menyu ")
        verbose_name_plural = _("4. Header Menyu")
    


class UsefulLink(ActiveModel, BaseModel):
    title = models.CharField(_("sarlavhasi"), max_length=256)
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
        verbose_name = _("Foydali manba ")
        verbose_name_plural = _("5. Foydali manbalar")







class Quote(SingletonModel, BaseModel):
    quote = models.TextField(verbose_name=_("iqtibos"))
    full_name = models.CharField(max_length=256, verbose_name=_("F.I.SH"))
    job = models.CharField(max_length=256, verbose_name=_("kasbi"))
    image = ImageField(upload_to=generate_upload_path, verbose_name=_("rasmi"))

    @property
    def get_image(self):
        if self.image:
            return f"{settings.HOST}{self.image.url}"

    @property
    def short_full_name(self):
        return truncatechars(self.full_name, 30)

    short_full_name.fget.short_description = _("F.I.SH")  # type: ignore # noqa: F401

    @property
    def short_quote(self):
        return truncatechars(self.quote, 200)

    short_quote.fget.short_description = _("iqtibos")  # type: ignore # noqa: F401

    class Meta:
        verbose_name = _("Iqtibos ")
        verbose_name_plural = _("6. Iqtibos")





class CharityProject(SingletonModel , BaseModel):
    title = models.CharField(max_length=256, verbose_name=_("sarlavhasi"), unique=True)
    description = models.TextField(max_length=512, verbose_name=_("batafsil"))
    logo = models.FileField(_("logotipi(.svg)") , upload_to=generate_upload_path)
    app_store_url = models.URLField(verbose_name=_("app store havolasi"))
    google_play_url = models.URLField(verbose_name=_("google play havolasi"))
    

    def __str__(self):
        return f"{self.title}"

    @property
    def short_title(self):
        return truncatechars(self.title, 30)

    short_title.fget.short_description = _("sarlavhasi")  # type: ignore # noqa: F401

    @property
    def get_logo(self):
        if self.logo:
            return f"{settings.HOST}{self.logo.url}"

    class Meta:
        verbose_name = _("Xayriya loyihasi ")
        verbose_name_plural = _("7. Xayriya loyihasi")


#     Misol:

# Loyiha: Water for Life
# Batafsil: Ushbu loyiha ichimlik suvi yetkazib berish uchun ishlaydi.
# Logotip: 🌊
# App Store: Havola
# Google Play: Havola




class NewsletterEmail(BaseModel):
    email = models.EmailField(verbose_name=_("email"), unique=True)

    def __str__(self):
        return f"{self.email}"
    
    class Meta:
        verbose_name = _("Yangiliklar uchun obuna emaili ")
        verbose_name_plural = _("8. Yangiliklar uchun obuna emaili")



class InstagramPhoto(BaseModel):
    img = ImageField(_("Rasm") , upload_to="images/" , blank=True , null=True)
    link = models.URLField(_("Link") , max_length=5000 , null=True , blank=True)

    class Meta:
        verbose_name = _("Instagram rasm")
        verbose_name_plural = _("9. Instagram rasm")

    @property
    def get_img(self):
        if self.img:
            return f"{settings.HOST}{self.img.url}"

    def __str__(self):
        return f"{self.link}"




class MusofirDonation(ActiveModel , BaseModel):
    amount = models.PositiveBigIntegerField(verbose_name=_("miqdor"))
    date = models.DateTimeField(verbose_name=_("sanasi"))
    note = models.CharField(verbose_name=_("Eslatma") , max_length=255)
    file = models.FileField(verbose_name=_("hujjat") , upload_to=generate_upload_path)
    
    
    @property
    def get_file(self):
        if self.file:
            return f"{settings.HOST}{self.file.url}"

    class Meta:
        ordering = ("-date",)
        verbose_name = _("Chiqim ")
        verbose_name_plural = _("Chiqimlar")




    