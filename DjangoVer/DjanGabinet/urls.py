from django.urls import path
from . import views
# Url Conf
urlpatterns = [
    path('testd/', views.testd ,name="testd"),
    path('main/' , views.main  ,name="main"),
    path('logn/' , views.logn  ,name="logn"),
    path('rgst/' , views.rgst  ,name="rgst"),
    path('dev/' , views.dev    ,name="dev"),

    path('panel_cnnk/' , views.panel_cnnk    ,name="panel_cnnk"),
    path('panel_czat/' , views.panel_czat    ,name="panel_czat"),
    path('panel_info/' , views.panel_info    ,name="panel_info"),
    path('panel_kale/' , views.panel_kale    ,name="panel_kale"),
    path('panel_pacj/' , views.panel_pacj    ,name="panel_pacj"),
    path('panel_sttg/' , views.panel_sttg    ,name="panel_sttg"),
    path('panel_wizt/' , views.panel_wizt    ,name="panel_wizt"),
    #VERY DIRTY PATRZ VIEWS
    path('panel_cnnk/' , views.panel_cnnk2    ,name="panel_cnnk2"),
    path('panel_czat/' , views.panel_czat2    ,name="panel_czat2"),
    path('panel_info/' , views.panel_info2    ,name="panel_info2"),
    path('panel_kale/' , views.panel_kale2    ,name="panel_kale2"),
    path('panel_pacj/' , views.panel_pacj2    ,name="panel_pacj2"),
    path('panel_sttg/' , views.panel_sttg2    ,name="panel_sttg2"),
    path('panel_wizt/' , views.panel_wizt2    ,name="panel_wizt2"),
]