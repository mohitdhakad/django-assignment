import django_filters
from tasklist.models import addtask


class datefilter(django_filters.FilterSet):
    class Meta:
        model = addtask
        fields = ['time',]