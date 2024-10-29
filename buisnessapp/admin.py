from django.contrib import admin
from .models import businessproposal, contact,query

# Register your models here.
admin.site.register(businessproposal)
admin.site.register(query)
admin.site.register(contact)