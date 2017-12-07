from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic import RedirectView
#from StudentSite import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'KentCollabCheckout.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^caladmin/', include(admin.site.urls)),
    url(r'^collabcheckout/', include('CollabCheckout.urls')),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/kentdenver.png')),

)
