from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('passPara/', views.passPara),
    path('hook', views.hook),
    path('invite', views.invite)
]