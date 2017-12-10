from django.conf.urls import url
from .import views

app_name = 'music'

urlpatterns = [
    #/music/        <--- link url nya
    url(r'^$', views.IndexView.as_view(), name='index'), #auto load first

    #/register/        <--- link url nya
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    #/music/album.id/       <--- link url nya
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #/music/album/add/       <--- link url nya
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    #/music/album/album.id/       <--- link url nya
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    #/music/album/album.id/delete       <--- link url nya
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

]
