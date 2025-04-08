from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


phone_validator = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message=_(
        "15 ta raqamga ruhsat berilgan. Standart raqam talab qilinadi",
    )
)