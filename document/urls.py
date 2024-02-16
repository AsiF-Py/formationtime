from django.urls import path
from . import views

urlpatterns = [
    path('document/',views.document_list),
    path('invoice/',views.invoice_list),
    path('support/',views.support,name='support'),
    path('join-support/',views.create_support,name='create_support'),
    ]