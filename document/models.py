from django.db import models
from account.models import Account
STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('cancel', 'Cancel'),
    ]

# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=250,null=True,blank=True)
    status = models.CharField(max_length=40,choices=STATUS_CHOICES,null=True,blank=True)
    state = models.CharField(max_length=200,null=True,blank=True)
    address = models.TextField()
    company_name = models.CharField(max_length=250,null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    attachment = models.FileField(upload_to='document/',null=True,blank=True)

    def __str__(self):
        return self.title

Invoice_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('cancel', 'Cancel'),
    ]
class Invoice(models.Model):
    id = models.CharField(primary_key=True, max_length=10,editable=False)
    due_date = models.DateField(blank=True,null=True)
    created = models.DateField(auto_now=True)
    description = models.TextField(blank=True,null=True)
    amount = models.IntegerField()
    status = models.CharField(max_length=20,choices=Invoice_STATUS_CHOICES,blank=True,null=True)
    attachment = models.FileField(upload_to='invoice/',blank=True,null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            last_invoice = Invoice.objects.order_by('-id').first()
            if last_invoice:
                last_id = int(last_invoice.id)
                self.id = '{:04d}'.format(last_id + 1)
            else:
                self.id = '0001'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.id


Support_STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('In Progress', 'In Progress'),
    ('Resolved', 'Resolved'),
    ('Closed', 'Closed'),
]
class Support(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    problem = models.TextField()
    solution = models.TextField(blank=True,null=True)

    status = models.CharField(max_length=30,choices=Support_STATUS_CHOICES,default='Pending')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)