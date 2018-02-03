from django.conf.urls import url 
from django.views.static import serve
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^imgupload/$', views.imgupload, name='imgupload'),
    url(r'^pics/(?P<path>.*)$', serve, {'document_root': 'pics'}),

] #+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

#index is the landing page.
# r represents regular expression
