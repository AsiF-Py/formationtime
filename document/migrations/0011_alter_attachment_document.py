# Generated by Django 5.0.2 on 2024-03-05 10:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0010_remove_document_attachment_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='document.document'),
        ),
    ]