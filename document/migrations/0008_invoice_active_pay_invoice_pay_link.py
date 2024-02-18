# Generated by Django 5.0.2 on 2024-02-18 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0007_remove_document_address_remove_document_company_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='active_pay',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='invoice',
            name='pay_link',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]
