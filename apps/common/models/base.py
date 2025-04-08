from unidecode import unidecode

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
from django.utils.translation import get_language
from apps.common.models.fields import ActiveField
from apps.common.models.managers import ActiveManager



class BaseModel(models.Model):    # Sana maydonlarini qoshish uchun... Boshqa modellarga created_at va updatet_at qoyish shartmas.  shu classdan inheritance olinsa boldi
    created_at = models.DateTimeField(_('Kiritilgan sana'), auto_now_add=True)
    updated_at = models.DateTimeField(_("o'zgartrilgan sana"), auto_now=True)

    class Meta:
        abstract = True



class Slugify(models.Model):  # Slug yaratish uchun.. yani berilgan matndan slug yaratish uchun foydalaniladi..Agar slug oldin ishlatilgan bo‘lsa, -1, -2, -3 kabi raqamlarni qo‘shib unikal qiladi
    slug = models.SlugField(_("slug"),max_length=255 , blank=True , null=True , unique=True)
    SLUG_FORM_FIELD = None    # qaysi maydondan hosil bolish kerakligini belgilaydi
  
    #  Agar title="Django ORM" bo‘lsa, slug="django-orm" bo‘ladi.

    class Meta:
        abstract = True
    
    def _make_slug(self , value):
        if value is not None:
            original_slug = slugify(unidecode(value))
            unique_slug = original_slug
            
            num=1
            while self.__class__.objects.exclude(pk=self.pk).filter(slug=unique_slug).exists():
                unique_slug = f"{original_slug}-{num}"
                num+=1
            return slugify(unique_slug)
        
    
    def save(self , *args , **kwargs):
        if self.slug is None:
            value_for_slug = getattr(self , self.SLUG_FROM_FIELD)
            self.slug = self._make_slug(value_for_slug)
        return super().save(*args , **kwargs)
        


class MultiLangSlugify(Slugify):  # bu tilga bogliq slug yaratish. bir nechta tilga mos slug yaratish imkonini beradi.
    slug_from_lang = models.CharField(
        choices=settings.MODELTRANSLATION_LANGUAGES_CHOICES,
        max_length=64,
        verbose_name=_("slugning tilini tanlash"),
        null=True,
        blank=True,
    )

    #  Slug yaratishda qaysi tilni ishlatish kerakligini tanlash imkonini beradi.
    # Agar til belgilanmagan bo‘lsa, joriy faol til (get_language()) ishlatiladi.


    class Meta:
        abstract = True
    
    def save(self, *args, **kwargs):
        if self.slug_from_lang is not None:
            value_for_slug = getattr(self, f"{self.SLUG_FROM_FIELD}_{self.slug_from_lang}")
            self.slug = self._make_slug(value_for_slug)

        if self.slug is None and self.slug_from_lang is None:
            self.slug_from_lang = get_language()   
        return super().save(*args, **kwargs)
    



class SingletonModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)  # MyModel.objects.all()   faqat active=True bo'lgan obyektlar
# Endi bu orqali faqat active=True bo'lgan obyektlar qaytariladi:
    
    def all_objects(self):
        # Bu barcha obyektlarni, shu jumladan active=False bo'lganlarini ham qaytaradi
        return models.QuerySet(self.model , using=self._db) # MyModel.objects.all_objects()
    




class SingletonModel(models.Model):
    active = ActiveField()
    objects = SingletonModelManager()

    class Meta:
        abstract = True
        unique_together = (("id",),) #   ya'ni har bir modelda id qiymati faqat bitta bo'lishi kerak.
    
    def save(self , *args , **kwargs):
        self.pk = 1
        self.active = True
        super().save(*args , **kwargs)


    @property
    def single_str(self):
        return str(self)
    
    #Django Admin'da ushbu maydon uchun qisqa tavsif qo‘shish mumkin.
    single_str.fget.short_description = ""    # type: ignore # noqa: F401

    @classmethod
    def get_solo(cls):
        return cls.objects.get_or_create(pk=1)[0]  # bu tuple qayataradi , 0 qiymat , 1 bool 
    


class ActiveModel(models.Model):
    objects = ActiveManager()
    active =  ActiveField()


    class Meta:
        abstract = True




    










            
            