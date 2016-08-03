from django.contrib import admin
from jaguar.models import Customer, Archive, Link, LinkHistory


# Customer
admin.site.register(Customer)


# Archive
class ArchiveLinkInline(admin.TabularInline):
    model = Link
    extra = 0
    fields = ('enabled', 'customer')
    readonly_fields = ('enabled', 'customer')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, nose):
        return False


class ArchiveAdmin(admin.ModelAdmin):
    list_display = ('filename', 'status', 'description','notes' )
    # list_display_links = None  not allowed until dh 1.7
    readonly_fields = ('filename', 'status', )
    inlines = [ArchiveLinkInline]

    def has_add_permission(self, request):
        return False


admin.site.register(Archive, ArchiveAdmin)


# Link
class LinkLinkHistoryInline(admin.TabularInline):
    model = LinkHistory
    extra = 0
    readonly_fields = ('country', 'city', 'dns', 'link', 'when', 'ip', )

    def has_add_permission(self, request):
        return False


class LinkAdmin(admin.ModelAdmin):
    list_display = ['archive', 'customer', 'enabled', 'url']
    list_filter = ['enabled']

    readonly_fields = ('url', )
    fields = ['url', 'archive', 'customer', 'enabled']
    inlines = [LinkLinkHistoryInline]

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('archive', 'customer', )
        return self.readonly_fields

admin.site.register(Link, LinkAdmin)


# LinkHistory
class LinkHistoryAdmin(admin.ModelAdmin):
    list_display = ['when', 'FileName', 'CustomerName',
                    'country', 'city', 'dns', 'ip', ]
    readonly_fields = ('link', 'when', 'FileName', 'CustomerName',
                       'country', 'city', 'dns', 'ip',)

    def has_add_permission(self, request):
        return False


admin.site.register(LinkHistory, LinkHistoryAdmin)
#    def has_change_permission(self, request):
#        return False
