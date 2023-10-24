from django.urls import path
from my_app.views import *

urlpatterns = [

    path("", index_view, name='index'),

]
