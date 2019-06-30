from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', formpage, name="formpage"),
    url(r'^cpdf.pdf$', DetailsPDF.as_view(), name="cpdf"),
    url(r'^cus_detail.html$', cus_details, name="cus_details"),
]