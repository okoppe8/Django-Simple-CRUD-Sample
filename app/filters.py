from django_filters import filters
from django_filters import FilterSet
from .models import Item


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'


class ItemFilter(FilterSet):

    name = filters.CharFilter(name='name', label='氏名', lookup_expr='contains')
    memo = filters.CharFilter(name='memo', label='備考', lookup_expr='contains')

    order_by = MyOrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('name', 'name'),
            ('age', 'age'),
        ),
        field_labels={
            'name': '氏名',
            'age': '年齢',
        },
        label='並び順'
    )

    class Meta:

        model = Item
        fields = ('name', 'sex', 'memo',)
