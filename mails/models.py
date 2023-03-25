from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model): 
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class IncomingMail(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    diary_no = models.IntegerField(null=True)
    reference_no = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    from_city = models.CharField(max_length=200, null=True)
    to_whom_marked = models.CharField(max_length=200)
    annotation = models.CharField(max_length=200, null=True)
    sign_by = models.CharField(max_length=200, null=True)
    sign_date = models.CharField(max_length=200, null=True)
    year_of_transcation = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.diary_no)
    
    # Ordering by date_created field
    class meta:
        ordering = ['-date_created']


class OutgoingMail(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    diary_no = models.IntegerField(null=True)
    reference_no = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    file_ref_date = models.CharField(max_length=200, null=True)
    from_city = models.CharField(max_length=200, null=True)
    subject = models.CharField(max_length=200, null=True)
    disposal = models.CharField(max_length=200, null=True)
    sign_by = models.CharField(max_length=200, null=True)
    sign_date = models.CharField(max_length=200, null=True)
    year_of_transcation = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.diary_no)

    class meta:
        ordering = ['-date_created']


