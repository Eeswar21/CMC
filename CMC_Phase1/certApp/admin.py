from django.contrib import admin
from certApp.models import Certificate

# Register your models here.
class CertificateAdmin(admin.ModelAdmin):
    list = ['cname', 'cissuer', 'creceiver', 'cgivendate','cexpirydate','crenewalteam','cstatus']

admin.site.register(Certificate, CertificateAdmin)
