from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

# Create your models here.

class Account(AbstractUser):
    address = models.CharField(max_length=100,blank=True,null=True)
    phone = models.IntegerField(blank=True,null=True)
    date_end = models.DateTimeField(blank=True,null=True)
    def save(self, *args, **kwargs):
        # Check if the password is set and not already hashed
        if self.password and not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)


class Company(models.Model):
    user = models.OneToOneField(Account,on_delete=models.CASCADE,primary_key=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    company_site = models.URLField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    communication = models.TextField(blank=True, null=True)
    allow_changes = models.BooleanField(default=False)
    company_state = models.CharField(max_length=100, blank=True, null=True)
    ein_number = models.CharField(max_length=100, blank=True, null=True)
    ssn_itin_number = models.CharField(max_length=100, blank=True, null=True)
    sale_tax_id = models.CharField(max_length=100, blank=True, null=True)
    annual_report_filing_date = models.DateField(blank=True, null=True)
    irs_corporate_income_tax_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.company_name
