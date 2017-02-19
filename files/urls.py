from django.conf.urls import url
from files import views

urlpatterns = [
    url(r'^files/$', views.file_list, name='file_list'),
    # url(r'^files/(?P<pk>[0-9]+)/$', views.FileDetail.as_view()),
    url(r'^bumps/(?P<readings>.*)/$', views.BumpDetail.as_view()),
]