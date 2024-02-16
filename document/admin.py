from django.contrib import admin
from .models import Document,Invoice,Support
# Register your models here.
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    pass

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    pass
@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    pass