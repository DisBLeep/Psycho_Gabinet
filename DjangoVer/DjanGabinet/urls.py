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
]