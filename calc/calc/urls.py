from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'calc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^add/(?P<num1>\d+)/(?P<num2>\d+)', 'calcapp.views.add'),
    url(r'^sub/(?P<num1>\d+)/(?P<num2>\d+)', 'calcapp.views.sub'),
    url(r'^mul/(?P<num1>\d+)/(?P<num2>\d+)', 'calcapp.views.mul'),
    url(r'^div/(?P<num1>\d+)/(?P<num2>\d+)', 'calcapp.views.div'),
)
