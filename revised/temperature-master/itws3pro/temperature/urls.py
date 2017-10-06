from django.conf.urls import include,url
from . import views
urlpatterns = [
    url(r'^$', views.index ,name = "index") ,
    url(r'^get/$', views.getdata ,name ="get"),
    url(r'^1.html',views.html,name = '1.html'),
    url(r'^001.html',views.html1,name = '001.html'),
    url(r'^002.html',views.html2,name = '002.html'),
]
