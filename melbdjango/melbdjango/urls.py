from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'members.views.member_signin', name='home'),
    url(r'^posts/', include('posts.urls', namespace='post')),
    url(r'^hacks/', include('hacks.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'django.shortcuts.render', {'template_name': 'index.html'}),
    url(r'^register/', 'members.views.member_registration', name='register'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
)
