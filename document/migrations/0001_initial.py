# Generated by Django 5.0.2 on 2024-02-12 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('status', models.CharField(choices=[('padding', 'Padding'), ('completed', 'Completed'), ('in_progress', 'In Progress'), ('cancel', 'Cancel')], max_length=40)),
                ('state', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('company_name', models.CharField(max_length=250)),
                ('date', models.DateField()),
                ('attachment', models.FileField(upload_to='document/')),
            ],
        ),
    ]
