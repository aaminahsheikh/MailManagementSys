import django_filters
from django_filters import DateFilter, CharFilter
from . models import *

class IncomingMailFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    end_date = DateFilter(field_name="date_created", lookup_expr='lte')
    #ref_no = CharFilter(field_name="reference_no", lookup_expr='icontains')
    class Meta:
        model = IncomingMail
        fields = '__all__'
        exclude = ['customer', 'date_created', 'to_whom_marked', 'annotation', 'sign_by', 'sign_date', 'year_of_transcation']


class OutgoingMailFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_created', lookup_expr='gte')
    end_date = DateFilter(field_name='date_created', lookup_expr='lte')

    class Meta:
        model = OutgoingMail 
        fields = '__all__'
        exclude = ['customer', 'date_created', 'subject', 'disposal', 'sign_by', 'sign_date', 'year_of_transcation']