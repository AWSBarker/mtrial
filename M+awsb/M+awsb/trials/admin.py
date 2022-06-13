# add export csv
from django.contrib import admin
from .models import Ctgov1, Contacts
from django.http import HttpResponse
from django.utils.html import format_html
import csv

class Ctgov1Admin(admin.ModelAdmin):
    fields = ('nct_id', 'drank_final', 'brief_title', 'overall_status', 'phase', 'enrollment', 'description', 'url', 'updated', 'ts',  'new', 'emailab', 'action', 'alloc', 'notes')
    list_display = ('nct_id', 'url_brief_title', 'drank_final', 'enrollment', 'updated', 'notes', 'get_username',)
    list_filter = (['updated', 'alloc__username'])
    search_fields = ('nct_id','brief_title', 'official_title', 'description',)
    ordering = ('-drank_final',)
    search_help_text = 'Search by Trial ID, or text in Brief/Official title, Description.............?'

    @admin.display(description='username')
    def get_username(self, obj):
        return f"{obj.alloc.username}"

class CountryListFilter(admin.SimpleListFilter):
    title = 'title'
    parameter_name =  'ending in .'

    def lookups(self, request, model_admin):
        lus =(
            ('FR', 'France'),
            ('GB', 'UK'),
            ('IT', 'Italy'),
        )
        return lus

    def queryset(self, request, queryset):
        if self.value() == 'FR':
            return queryset.filter(email__endswith='fr')
        if self.value() == 'GB':
            return queryset.filter(email__endswith='uk')
        if self.value() == 'IT':
            return queryset.filter(email__endswith='it')

@admin.action(description='Export to CSV')
def export_csv(modeladmin, request, queryset):
    print('admin worked')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="contacts.csv"'
    writer = csv.writer(response)
    writer.writerow(['nct_id', 'contact_type', 'name', 'phone', 'email'])
    cs = queryset.values_list('nct_id', 'contact_type', 'name', 'phone', 'email')
    for c in cs:
        writer.writerow(c)
    return response


class ContactsAdmin(admin.ModelAdmin):
    fields = ('nct_id', 'name', 'phone', 'email',)
    list_display = ('url_nct_id', 'name', 'phone', 'email',)
    list_filter = (CountryListFilter,)
    search_fields = ('name', 'email', 'nct_id__nct_id',)
    #ordering = ('-ncd_id',)
    search_help_text = 'Search by Trial NCT_ID, Contacts, email.............?'
    actions = [export_csv,]

    @admin.display(description='Trial ID')
    def url_nct_id(self, obj):
        return format_html("<a href={} target=_blank>{}</a>", obj.nct_id.url, obj.nct_id.nct_id)


admin.site.register(Ctgov1, Ctgov1Admin)
admin.site.register(Contacts, ContactsAdmin)
#admin.site.site_header = "M+ Hub API : Device, Trials admin panels"

'''nct_id, drank_final, brief_title, overall_status, phase, enrollment, description, url, updated, ts,  new, emailab, action, notes,alloc
class Contacts(models.Model):
    id = models.AutoField(primary_key=True, max_length=12)
    nct_id = models.CharField(max_length=12, blank=True, null=True)
    contact_type = models.CharField(max_length=12)
    name = models.CharField(max_length=36, null=True)
    phone = models.CharField(max_length=36, null=True)
    email = models.CharField(max_length=36, null=True)


'''
