from django.contrib import admin

from jaguar.models import Customer, Archive, Link

# Register your models here.

admin.site.register(Customer)

admin.site.register(Archive)


class LinkAdmin(admin.ModelAdmin):
    fields = [ 'archive','customer','expiryDate']
    list_display = ['archive','customer','expiryDate','url' ]
    list_filter = ['expiryDate']


#admin.site.register(Link)
admin.site.register(Link,LinkAdmin)
