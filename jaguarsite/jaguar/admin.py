from django.contrib import admin

from jaguar.models import Customer, Archive, Link, LinkHistory

# Register your models here.

admin.site.register(Customer)



class ArchiveAdmin(admin.ModelAdmin):
    readonly_fields = ('filename','status',)

    def has_add_permission(self, request):
        return False

admin.site.register(Archive,ArchiveAdmin)



class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('url',)
    fields = [ 'url','archive','customer','enabled']
    list_display = ['archive','customer','enabled','url' ]
    list_filter = ['enabled']


#admin.site.register(Link)
admin.site.register(Link,LinkAdmin)



admin.site.register(LinkHistory)
