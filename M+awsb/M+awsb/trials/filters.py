from .models import Ctgov1
import django_filters

class Ctgov1Filter(django_filters.FilterSet):
    nct_id = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Ctgov1
        fields = ['nct_id', 'alloc', 'description']

    @property
    def qs(self):
        parent = super().qs
        #author = getattr(self.request, 'user', None)
        return parent.filter(drank_final__gte = 140)
