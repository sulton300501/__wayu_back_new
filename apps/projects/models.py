from ckeditor_uploader.fields import RichTextUploadingField
from sorl.thumbnail import ImageField

from django.conf import settings
from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.translation import gettext_lazy as _

from apps.common.models.base import ActiveModel, BaseModel, MultiLangSlugify
from apps.common.models.fields import OrderField
from apps.common.utils import generate_upload_path






class Project(ActiveModel, MultiLangSlugify, BaseModel):
    title = models.CharField(verbose_name=_("nomi"), max_length=255)
    logo = models.FileField(verbose_name=_("loyiha logosi"), upload_to=generate_upload_path)
    SLUG_FROM_FIELD = "title"  # type: ignore # noqa: F401
    order = OrderField()

    class Meta:
        verbose_name = "Loyiha "
        verbose_name_plural = "1. Loyihalar"

    @property
    def get_logo(self):
        if self.logo:
            return f"{settings.HOST}{self.logo.url}"

    @property
    def short_name(self):
        return truncatechars(self.title, 30)

    short_name.fget.short_description = _("nomi")  # type: ignore # noqa: F401

    def __str__(self):
        return self.title
    



class Introduction(BaseModel):
    project = models.OneToOneField(
        Project, on_delete=models.CASCADE, verbose_name=_("loyiha"), related_name="projects", null=True
    )
    image = ImageField(verbose_name=_("rasmi"), upload_to=generate_upload_path)
    icon = models.FileField(verbose_name=_("belgisi(.svg"), upload_to=generate_upload_path)
    title = models.TextField(verbose_name=_("sarlavhasi"), max_length=511)
    text = RichTextUploadingField(verbose_name=_("batafsil"))

    @property
    def get_icon(self):
        if self.icon:
            return f"{settings.HOST}{self.icon.url}"

    @property
    def get_image(self):
        if self.image:
            return f"{settings.HOST}{self.image.url}"

    @property
    def short_name(self):
        return truncatechars(self.title, 30)

    short_name.fget.short_description = _("nomi")  # type: ignore # noqa: F401

   
    def __str__(self):
        return "%s" % self.title
    

    class Meta:
        verbose_name = "Kirish "
        verbose_name_plural = "2. Kirish"

    


class AboutProject(BaseModel):
    project = models.OneToOneField(
        Project, on_delete=models.CASCADE, verbose_name=_("Loyiha"), related_name="calendarplans"
    )
    title = models.CharField(max_length=255, verbose_name=_("sarlavhasi"))
    text = RichTextUploadingField(verbose_name=_("batafsil"))
    image = ImageField(verbose_name=_("rasmi"), upload_to=generate_upload_path)
    youtube_url = models.URLField(max_length=255, verbose_name=_("youtubedan havola"))

    @property
    def get_image(self):
        if self.image:
            return f"{settings.HOST}{self.image.url}"

    def __str__(self):
        return self.title

    @property
    def short_name(self):
        return truncatechars(self.title, 30)

    short_name.fget.short_description = _("nomi")  # type: ignore # noqa: F401

    class Meta:
        verbose_name = "Loyiha haqida "
        verbose_name_plural = "3. Loyiha haqida "







class GoalAndMission(ActiveModel, BaseModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name=_("Loyiha"), related_name="ratings")
    title = models.CharField(max_length=511, verbose_name=_("Sarlavha"))
    icon = models.FileField(verbose_name=_("belgisi(.svg)"), upload_to=generate_upload_path)
    text = models.TextField(verbose_name=_("batafsil"))
    order = OrderField()

    @property
    def get_icon(self):
        if self.icon:
            return f"{settings.HOST}{self.icon.url}"

    class Meta:
        ordering = ("order",)
        verbose_name = "Maqsad va vazifa "
        verbose_name_plural = "4. Maqsad va vazifalar "

    @property
    def short_name(self):
        return truncatechars(self.title, 30)

    short_name.fget.short_description = _("nomi")  # type: ignore # noqa: F401







class Document(ActiveModel , BaseModel):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, verbose_name=_("Loyiha"), related_name="documents", null=True
    )
    title = models.CharField(verbose_name=_("hujjat nomi"), max_length=512)
    file = models.FileField(verbose_name=_("hujjat fayli"), upload_to=generate_upload_path)
    type = models.CharField(max_length=6)
    file_size = models.FloatField(verbose_name=_("hujjat hajmi"), default=0)
    order = OrderField()


    def clean(self):
        self.file_size = self.file.size
        t = self.file.path
        t = t.split(".")
        self.type = t[-1]
        return self
    

    def __str__(self):
        return self.title

    @property
    def get_file(self):
        if self.file:
            return f"{settings.HOST}{self.file.url}"

    @property
    def short_title(self):
        return truncatechars(self.title, 30)

    short_title.fget.short_description = _("sarlavha")  # type: ignore # noqa: F401

    class Meta:
        ordering = ("order",)
        verbose_name = _("Hujjat ")
        verbose_name_plural = _("5. Hujjatlar")
    






class ProjectDocument(BaseModel):
    project = models.OneToOneField(
        Project, on_delete=models.CASCADE, verbose_name=_("Loyiha"), related_name="projectdocuments"
    )
    title = models.CharField(max_length=511, verbose_name=_("Sarlavha"))
    text = models.TextField(verbose_name=_("batafsil"))

    @property
    def short_title(self):
        return truncatechars(self.title, 30)

    short_title.fget.short_description = _("sarlavha")  # type: ignore # noqa: F401

    class Meta:
        verbose_name = _("Hujjat ")
        verbose_name_plural = _("6. Loyiha Hujjatlari")






class TeamMember(BaseModel):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, verbose_name=_("Loyiha"), related_name="projectmembers", null=True
    )
    full_name = models.CharField(max_length=100, verbose_name=_("Ism-familiyasi"), null=True)
    position = models.CharField(max_length=100, verbose_name=_("Lavozimi"), null=True)
    email = models.EmailField("E-maili", null=True)
    avatar = ImageField(verbose_name=_("Rasmi"), upload_to=generate_upload_path)
    order = OrderField()

    @property
    def get_avatar(self):
        if self.avatar:
            return f"{settings.HOST}{self.avatar.url}"

    class Meta:
        verbose_name = _("Jamoa a'zolari ")
        verbose_name_plural = _("7. Jamoa a'zolari")


class FeedbackProjects(BaseModel):
    full_name = models.CharField(max_length=255, verbose_name=_("F.I.SH"))
    email = models.EmailField(max_length=255, verbose_name=_("email pochta"))
    message = models.TextField(verbose_name=_("xabar"))
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name=_("loyiha"), null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _("Fikr ")
        verbose_name_plural = _("8. Fikrlar")
