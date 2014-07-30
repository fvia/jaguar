from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from jaguar import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jaguarsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'jaguar.views.index', name='index'),
    url(r'^jaguar/ReloadArchives$', 'jaguar.views.ReloadArchives',name='ReloadArchives'),
    url(r'^admin/', include(admin.site.urls)),
)
