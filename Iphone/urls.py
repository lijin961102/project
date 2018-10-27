from django.conf.urls import url

from Iphone import views
app_name = 'Iphone'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r"^test/j/$",views.test,name='test'),
    url(r'^register/$',views.register),
    url(r'^login/$',views.login),
    url(r'^logout/$',views.logout),
    url(r'^cart/$',views.cart),

]