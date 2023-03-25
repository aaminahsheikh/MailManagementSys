from django.contrib import admin
from . models import Customer, IncomingMail, OutgoingMail

# Register your models here.
admin.site.register(Customer)
admin.site.register(IncomingMail)
admin.site.register(OutgoingMail)