from django.contrib import admin
     
# Register your models here.
from contact.models import (listemail, formcontact)
admin.site.register(listemail)
admin.site.register(formcontact)