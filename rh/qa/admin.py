from django.contrib import admin
from .models import Employee
from .models import Company
from .models import Employment
from .models import Relationship
from .models import CompanyInformations

admin.site.register(Employee)
admin.site.register(Company)
admin.site.register(Employment)
admin.site.register(Relationship)
admin.site.register(CompanyInformations)
# Register your models here.
