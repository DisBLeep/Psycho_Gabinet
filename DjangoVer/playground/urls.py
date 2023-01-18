from django.urls import path
from . import views
# Url Conf
urlpatterns = [
    path('hello/', views.say_hello),
    path('panel/', views.panel),
    path('test/', views.test)
]