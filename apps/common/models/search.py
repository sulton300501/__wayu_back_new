# from django.db import models
# from django.utils.translation import gettext_lazy as _
# from apps.news.models import Event, News
# from django.dispatch import receiver
# from django.db.models.signals import post_save


# class ObjTypes(models.TextChoices):
#     event = "event", _("Tadbir")
#     news = "news", _("Yangilik")


# class SearchModel(models.Model):
#     obj_type = models.CharField(max_length=255, choices=ObjTypes.choices)

#     event = models.ForeignKey(Event, null=True, blank=True, on_delete=models.CASCADE)
#     news = models.ForeignKey(News, null=True, blank=True, on_delete=models.CASCADE)

#     created_at = models.DateTimeField(null=True, blank=True)

#     def __str__(self):
#         return "Global Search"


# @receiver(post_save, sender=Event)
# def event_post_save(sender, instance, **kwargs):
#     search = SearchModel.objects.get_or_create(obj_type=ObjTypes.event, event=instance)
#     search[0].created_at = instance.created_at
#     search[0].save()


# @receiver(post_save, sender=News)
# def news_post_save(sender, instance, **kwargs):
#     search = SearchModel.objects.get_or_create(obj_type=ObjTypes.news, news=instance)
#     search[0].created_at = instance.created_at
#     search[0].save()
