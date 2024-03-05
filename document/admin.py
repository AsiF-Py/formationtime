from django.contrib import admin
from .models import Document,Invoice,Support,Attachment
# Register your models here.
class AttachmentAdmin(admin.TabularInline):
    model = Attachment
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['user','title','date']
    list_editable = ['title','date']
    list_display_links = ['user']
    list_filter = ['user','date']
    inlines = [AttachmentAdmin]
@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'due_date', 'created','amount','attachment','active_pay']
    list_editable = ['due_date', 'attachment','active_pay','amount']
    list_display_links = ['id','user']
    list_filter = ['user','active_pay' ,'due_date']
@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    pass