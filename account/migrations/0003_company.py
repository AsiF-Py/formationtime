# Generated by Django 5.0.2 on 2024-02-18 19:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_account_address_alter_account_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('industry', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('contact_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('company_site', models.URLField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('communication', models.TextField(blank=True, null=True)),
                ('allow_changes', models.BooleanField(default=False)),
                ('company_state', models.CharField(blank=True, max_length=100, null=True)),
                ('ein_number', models.CharField(blank=True, max_length=100, null=True)),
                ('ssn_itin_number', models.CharField(blank=True, max_length=100, null=True)),
                ('sale_tax_id', models.CharField(blank=True, max_length=100, null=True)),
                ('annual_report_filing_date', models.DateField(blank=True, null=True)),
                ('irs_corporate_income_tax_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]