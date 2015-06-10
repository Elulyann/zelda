from django.contrib import admin
from contacts.models import Title, Contact, Categorie

admin.site.register(Contact)
admin.site.register(Title)
admin.site.register(Categorie)

