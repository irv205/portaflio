from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'email', 'message', 'job_offer')

admin.site.register(Contact, ContactAdmin)