from django.contrib import admin
from audition.models import mydata

# changing admin panal headers
admin.site.site_header = 'SAE Audition'
# Register your models here.
admin.site.register(mydata)
