from django.urls import path
from . import views
# Url Conf
urlpatterns = [
    #path(''             , views.main    ,name="main"),
    path('panel/'       , views.panel   ,name="panel"),
    path('register/'    , views.register,name="register"),
]