# Generated by Django 5.0.2 on 2024-02-12 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0003_alter_document_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_number', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('due_date', models.DateField()),
                ('created', models.DateField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('amount', models.IntegerField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('in_progress', 'In Progress'), ('cancel', 'Cancel')], max_length=20)),
                ('attachment', models.FileField(upload_to='invoice/')),
            ],
        ),
        migrations.AlterField(
            model_name='document',
            name='status',
            field=models.CharField(blank=True, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('in_progress', 'In Progress'), ('cancel', 'Cancel')], max_length=40, null=True),
        ),
    ]
