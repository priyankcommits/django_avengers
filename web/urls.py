from django.conf.urls import url

from web.views.heroes import list_heroes
from web.views.heroes.create import HeroCreateView, HeroCreateModelView
from web.views.heroes.list import HeroListView


urlpatterns = [
    url(r'^hero/create/model/$', HeroCreateModelView.as_view(), name='hero_create_model'),
    url(r'^hero/create/$', HeroCreateView.as_view(), name='hero_create'),
    url(r'^hero/list/fbv/$', list_heroes, name='hero_list_fbv'),
    url(r'^$', HeroListView.as_view(), name='hero_list'),
]
