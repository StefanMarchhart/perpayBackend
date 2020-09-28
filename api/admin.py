from django.contrib import admin

# Register your models here.
from api.models import *

admin.site.register(Company)
admin.site.register(PerpayUser)
admin.site.register(Payment)
