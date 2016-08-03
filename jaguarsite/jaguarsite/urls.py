from django.conf.urls import patterns, include, url

from django.contrib import admin

from jaguar import views

admin.autodiscover()


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'jaguarsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'jaguar.views.index', name='index'),
    url(r'^jg/ReloadArchives$','jaguar.views.ReloadArchives',name='ReloadArchives'),
    
    url(r'^jaguar/jg/ReloadArchives$','jaguar.views.ReloadArchives',name='ReloadArchives'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^jaguar/admin/', include(admin.site.urls)), #needed for runserver


    url(r'^jaguar/downloads/$', 'jaguar.views.Downloads',name='Downloads'), #needed for runserver


    )
