from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.main'
    verbose_name = _("2. Asosiy sahifa")

    def ready(self):
        import apps.main.signals    # noqa: 401
