import django_filters
from tasklist.models import addtask


class datefilter(django_filters.FilterSet):
    class Meta:
        model = addtask
        fields = ['time',]

    def __init__(self, *args, **kwargs):
       super(datefilter, self).__init__(*args, **kwargs)
       self.filters['time'].label="enter date to filter task(yyyy-mm-dd)"