from django.conf.urls import url

from . import views


app_name = 'jitterbunk'
urlpatterns = [
    # ex: /jitterbunk
    #homepage, shows all bunks from all users
    url(r'^$', views.index, name='index'),

    # ex: /{user.id}
    url(r'^(?P<user_id>[0-9]+)/$', views.personalBunkFeed, name='personalBunkFeed'),

    # eg. /makeBunk/{user.id}
    url(r'^makeBunk/(?P<user_id>[0-9]+)/$', views.makeBunk, name='makeBunk'),

]