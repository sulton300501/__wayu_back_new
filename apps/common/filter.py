from django_filters import Filter , FilterSet

from apps.common.models import model


class M2MFilter(Filter):
    def __init__(self,*args , **kwargs):
        super().__init__(*args , **kwargs)


    def filter(self , qs , value):
        if not value:
            return qs
        values = value.split(",")
        values = [int(v) for v in values] 
        print(values)
        # for v in values:
        qs = qs.filter(tags__id__in=values)
        return qs
    

class FAQFilter(FilterSet):
    tags = M2MFilter()

    class Meta:
        model = model.FAQ
        fields = ("tags",)