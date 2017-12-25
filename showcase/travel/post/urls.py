from django.conf.urls import url
from django.contrib import admin
from post import views

urlpatterns = [
   # url(r'^admin/', admin.site.urls),
    #url(r'^$',views.index,name='index'),
    url(r'^$',views.aindex,name='aindex'),
    #url(r'^post/single/$',views.single,name='single'),
    url(r'^cindex/$',views.cindex,name='cindex'),
]
