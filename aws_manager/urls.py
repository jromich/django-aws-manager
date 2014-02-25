from aws_manager import views

# DJANGO IMPORTS
try:
    from django.conf.urls import url, patterns
except ImportError:
    # for Django version less then 1.4
    from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('',
    url(r'^get_rdp/(?P<public_dns>[\w|\W]+)/(?P<username>\w+)/$', 'aws_manager.views.get_rdp'),
)

