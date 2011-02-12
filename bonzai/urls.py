from django.conf.urls.defaults import *
from seo_monitor import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', views.home_page),
	(r'^signup/$', views.signup_page),
	(r'^login/$', views.login_page),
	(r'^logout/$', views.logout_page),
	(r'^user/(\w+)/$', user_page) # parens capture string that matches. pass to view. 
    # Example:
    # (r'^bonzai/', include('bonzai.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
