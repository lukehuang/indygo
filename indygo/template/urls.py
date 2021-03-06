from django.conf.urls.defaults import *
import settings.common as settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
	(r'', include('core.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': settings.MEDIA_ROOT})
)
