from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', custlist, name='list'),
    url(r'^insta_scrape$', insta_scrape, name='insta'),
    url(r'^fb_scrape$', fb_scrape, name='fb'),
]
