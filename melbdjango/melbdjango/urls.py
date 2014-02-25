from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'hacks.views.signin_request', name='home'),
    url(r'^posts/', include('posts.urls', namespace='post')),
    url(r'^hacks/', include('hacks.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'django.shortcuts.render', {'template_name': 'index.html'}),
    url(r'^register/', 'hacks.views.hacker_registration', name='register'),
    url(r'^logout/', 'hacks.views.logout_request', name='logout'),
)
