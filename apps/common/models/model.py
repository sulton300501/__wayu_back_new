import logging
from apps.common.models.base import BaseModel 
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models.base import ActiveModel   , SingletonModel , MultiLangSlugify
from apps.common.models.fields import OrderField  , PhoneField
from django.template.defaultfilters import truncatechars
from phonenumber_field.modelfields import PhoneNumberField
from django_better_admin_arrayfield.models.fields import ArrayField 
from django.utils.translation import gettext as _g
from django.dispatch import receiver
from django.db.models.signals import pre_save
from apps.common.helpers import get_long_lat
from sorl.thumbnail import ImageField
from apps.common.utils import generate_upload_path
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import JSONField
import requests








class FAQTag(BaseModel):
    title = models.CharField(max_length=255  ,verbose_name=_("sarlavha"))

    class Meta:
        verbose_name = _("Savol va javob tegi")
        verbose_name_plural = _("1. Savol va javob teglari")

    
    def __str__(self):
        return self.title
    



class FAQ(ActiveModel , BaseModel):
    question = models.TextField(verbose_name=_("Savol"))
    answer = models.TextField(verbose_name=_("Javob"))
    order = OrderField()
    tags = models.ManyToManyField("FAQTag", verbose_name=_("Teglar"))

    def __str__(self):
        return self.question + ": " + self.answer
    
    class Meta:
        ordering = ("order",)
        verbose_name = _("savol va javob")
        verbose_name_plural = _("2. Savollar va javoblar")

    @property
    def short_question(self):
        return truncatechars(self.question , 30)   # kiritilgan savol 30 ta belgidan keyin ... qoyip beradi... "Bu juda uzun savol bo‘lib, un..."
    
     
     # admin panelda column nomiga "savol" yoziladi
    short_question.fget.short_description = _("savol")  # type: ignore # noqa: F401
    


    @property
    def short_answer(self):
        return truncatechars(self.answer , 30)
    

    short_answer.fget.short_description = _("javob") # type: ignore # noqa: F401




class Application(BaseModel):
    full_name = models.CharField(max_length=256 , verbose_name=_("F.I.SH"))
    phone_number = PhoneNumberField(verbose_name=_("telefon raqam"))
    question = models.TextField(verbose_name=_("Yo'llangan savoli"))


    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = _("Kelib tushgan savol")
        verbose_name_plural = _("3. Kelip tushgan savollar")



@receiver(pre_save , sender=Application)
def save_feedback_phone_number(sender , instance ,*args , **kwargs):
    try:
        text = (
            "Kelip tushgan xabarlar\nn"
            f"*Ariza turi: * Biz bilan bog'lanish bo'limi\n"
            f"Toliq ism sharifi: {instance.full_name}"
            f"*Telefon raqami:* {instance.phone_number}\n"
            f"*Yo'llagan savoli:* {instance.question}\n"

        )

        url = f"https://api.telegram.org/bot{settings.API_KEY}" + "/sendMessage"

        requests.get(url, data={"chat_id": settings.CHAT_ID, "text": text, "parse_mode": "Markdown"})


    except Exception as e:
        logging.error(str(e))





class Contact(SingletonModel, BaseModel):
    title = models.CharField(max_length=256, verbose_name=_("sarlavha"))
    address = models.CharField(_("Yuridik manzili"), max_length=1024)
    emails = models.EmailField(_("elektron pochta"), unique=True)

    
    phones = PhoneNumberField(unique=True, verbose_name=_("telefon raqamlar"))

    main_phone_number = PhoneField(verbose_name=_("asosiy bog'lanish raqami"))
    location = models.URLField(verbose_name=_("xarita manzili"))
    latitude = models.CharField(_("kengligi"), max_length=128, null=True, blank=True)
    longitude = models.CharField(_("uzunligi"), max_length=128, null=True, blank=True)
    youtube = models.URLField(verbose_name=_("youtube"), null=True, blank=True)
    instagram = models.URLField(verbose_name=_("instagram"), null=True, blank=True)
    telegram = models.URLField(verbose_name=_("telegram"), null=True, blank=True)
    twitter = models.URLField(verbose_name=_("twitter"), null=True, blank=True)
    whatsapp = PhoneField(verbose_name=_("whatsapp raqami"), null=True, blank=True)

    def __str__(self):
        return _g("bog'lanish")

    class Meta:
        verbose_name = _("Bog'lanish ")
        verbose_name_plural = _("4. Bog'lanish")

    @property
    def short_title(self):
        return truncatechars(self.title, 30)

    short_title.fget.short_description = _("sarlavha")  # type: ignore # noqa: F401


@receiver(pre_save, sender=Contact)
def save_long_lat(sender, instance, *args, **kwargs):
    if instance.location is not None:
        res, status = get_long_lat(instance.location)
        if status is True:
            instance.latitude = res["lat"]
            instance.longitude = res["long"]





class Feedback(BaseModel):
    full_name = models.CharField(max_length=256 , verbose_name=_("F.I.SH"))
    phone_number = PhoneNumberField(verbose_name=_("telefon raqami"))
    email = models.EmailField(verbose_name=_("Elektron pochta"))
    message = models.TextField(verbose_name=_("Yo'llangan xabar"))


    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = _("Kelib tushgan xabar")
        verbose_name_plural = _("6. Kelib tushgan xabarlar")




@receiver(pre_save , sender=Feedback)
def save_feedback_phone_number(sender , instance ,*args , **kwargs):
    try:
        text = (
            "Kelip tushgan xabarlar\nn"
            f"*Ariza turi: * Biz bilan bog'lanish bo'limi\n"
            f"Toliq ism sharifi: {instance.full_name}"
            f"*Telefon raqami:* {instance.phone_number}\n"
            f"*Elektron pochtasi:* {instance.email}\n"
            f"*Yo'llagan savoli:* {instance.message}\n"

        )

        url = f"https://api.telegram.org/bot{settings.API_KEY}" + "/sendMessage"

        requests.get(url, data={"chat_id": settings.CHAT_ID, "text": text, "parse_mode": "Markdown"})


    except Exception as e:
        logging.error(str(e))



class ContactUser(SingletonModel , BaseModel):
    full_name = models.CharField(max_length=256, verbose_name=_("F.I.SH"))
    position = models.CharField(max_length=256, verbose_name=_("Lavozimi"))
    image = ImageField(verbose_name=_("rasmi"), upload_to=generate_upload_path)
    phone_number = PhoneNumberField(verbose_name=_("telefon raqami"))
    email = models.EmailField(verbose_name=_("elektron pochtasi"))
    reception_days = models.CharField(max_length=256, verbose_name=_("ish kunlari"))
    description = models.TextField(verbose_name=_("tavsif"))



    @property
    def get_image(self):
        if self.image:
            return f"{settings.HOST}{self.image.url}"
        
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = _("Bog'lanishga javobgar odam ")
        verbose_name_plural = _("5. Bog'lanishga javobgar odam")


class Country(ActiveModel , BaseModel):
    title = models.CharField(max_length=255, verbose_name=_("davlat nomi"))
    flag = ImageField(upload_to=generate_upload_path ,verbose_name=_("davlat bayrog'i"))

    @property
    def short_title(self):
        return truncatechars(self.title , 30)
    
    short_title.fget.short_description = _("sarlavha")

    @property
    def get_flag(self):
        if self.flag:
            return f"{settings.HOST}{self.flag.url}"
        
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("Davlat ")
        verbose_name_plural = _("7. Davlatlar ")


class Pages(ActiveModel , MultiLangSlugify , BaseModel):
    title = models.CharField(max_length=256, verbose_name=_("sarlavhasi"))
    content = RichTextUploadingField(verbose_name=_("mazmuni"))
    SLUG_FROM_FIELD = "title" # type: ignore # noqa: F401

    def __str__(self):
        return self.title

    @property
    def short_title(self):
        return truncatechars(self.title, 30)

    short_title.fget.short_description = _("sarlavha")  # type: ignore # noqa: F401

    class Meta:
        verbose_name = _("Statik sahifa ")
        verbose_name_plural = _("8. Statik sahifalar")

        











    

