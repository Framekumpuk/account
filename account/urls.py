from django.conf.urls import url

from . import views

app_name = 'account'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail$', views.income, name='income' ),
    url(r'^index$', views.expense, name='expense' ),
    url(r'^history$', views.history, name='history' ),
]
