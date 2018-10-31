from django.contrib import admin
from .models import Qa
from .models import Company
from .models import Employment

admin.site.register(Qa)
admin.site.register(Company)
admin.site.register(Employment)
# Register your models here.
