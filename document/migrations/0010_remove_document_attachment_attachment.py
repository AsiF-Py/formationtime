# Generated by Django 5.0.2 on 2024-03-05 10:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0009_support_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='attachment',
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(blank=True, null=True, upload_to='document/')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.document')),
            ],
        ),
    ]
