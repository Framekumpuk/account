from django.conf.urls import url

from . import views

app_name = 'account'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail$', views.operand, name='operand' ),
    url(r'^history$', views.history, name='history' ),
    url(r'^csv$', views.some_view, name='csv' ),
]
