from django.contrib import admin
from .models import Account,Company
# Register your models here.

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass