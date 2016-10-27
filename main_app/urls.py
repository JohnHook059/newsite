from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^feedback$', views.feedback, name='feedback'),
    url(r'^feedback_admin$', views.feedback_admin, name='feedback_admin'),
    url(r'^underdev$', views.underdev, name='underdev'),
    url(r'^osago$', views.osago, name='osago'),
    url(r'^kasko$', views.kasko, name='kasko'),
]