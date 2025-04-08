from django.db.models import IntegerField , BooleanField , CharField
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

from apps.common.validators import phone_validator


class OrderField(IntegerField):
    def __init__(self, verbose_name=_("tartibi"),default=1 , validators=None , **kwargs):
        if validators is None:
            validators = [MinValueValidator(1)]
        super().__init__(verbose_name=verbose_name , default=default, validators=validators , **kwargs)



class ActiveField(BooleanField):
    def __init__(self, verbose_name=_("aktiv") , default=False , **kwargs):
        super().__init__(verbose_name=verbose_name , default=default, **kwargs)


class PhoneField(CharField):
    def __init__(self, verbose_name=_("telefon raqam"), max_length=15 , validators=None , **kwargs):
        if validators is None:
            validators = [phone_validator]
        super().__init__(verbose_name=verbose_name ,max_length=max_length , validators=validators, **kwargs)
        



def phone_split(x):
    x = "+998" + x
    x = " ".join([x[0:4], x[4:6], x[6:13], x[13:]])
    x = "(".join([x[0:5], x[5:]])
    x = ")".join([x[0:8], x[8:]])
    x = "-".join([x[0:13], x[13:15], x[15:]])
    return x