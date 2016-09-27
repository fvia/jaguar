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

    url(r'^jg/LoadKeyUpdates$','jaguar.views.LoadKeyUpdates',name='LoadKeyUpdates'),
    url(r'^jaguar/jg/LoadKeyUpdates$','jaguar.views.LoadKeyUpdates',name='LoadKeyUpdates'),

    


    url(r'^admin/', include(admin.site.urls)),
    url(r'^jaguar/admin/', include(admin.site.urls)), #needed for runserver


    url(r'^jaguar/downloads/$', 'jaguar.views.Downloads',name='Downloads'), #needed for runserver
    url(r'^downloads/$', 'jaguar.views.Downloads',name='Downloads'),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'  } ),    
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/accounts/login'  } ),    

    # we are coming here after a sucessfull login
    url(r'^profiles/home', 'jaguar.views.home' ),    

    url(r'^jaguar/trialextension$', 'jaguar.views.TrialExtensionGet'), #needed for runserver
    url(r'^trialextension$', 'jaguar.views.TrialExtensionGet'),

    url(r'^jaguar/trialextensioninfo$', 'jaguar.views.TrialExtensionInfo'), #needed for runserver
    url(r'^trialextensioninfo$', 'jaguar.views.TrialExtensionInfo'),


    url(r'^jaguar/licenseupdate$', 'jaguar.views.LicenseUpdateGet'), #needed for runserver
    url(r'^licenseupdate$', 'jaguar.views.LicenseUpdateGet'),

    url(r'^jaguar/licenseupdateinfo$', 'jaguar.views.LicenseUpdateInfo'), #needed for runserver
    url(r'^licenseupdateinfo$', 'jaguar.views.LicenseUpdateInfo'),
 
    )
