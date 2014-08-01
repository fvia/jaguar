from django.contrib import admin

from jaguar.models import Customer, Archive, Link

# Register your models here.

admin.site.register(Customer)

admin.site.register(Archive)


class LinkAdmin(admin.ModelAdmin):
    fields = [ 'archive','customer','enabled']
    list_display = ['archive','customer','enabled','url' ]
    list_filter = ['enabled']


#admin.site.register(Link)
admin.site.register(Link,LinkAdmin)
