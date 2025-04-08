import django_filters

from . import models


class M2Mfilter(django_filters.Filter):
    def __init__(self , *args , **kwargs):
        super(M2Mfilter , self).__init__(*args , **kwargs)

    def filter(self , qs , value):
        if not value:
            return qs
        values = value.split(",")
        for i in values:
            qs = qs.filter(tags=i)
        return qs

    

class NewsFilter(django_filters.FilterSet):
    tags = M2Mfilter()

    class Meta:
        model = models.News
        fields = ("tags","category__slug","country__title")