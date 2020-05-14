from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="mainpage-index"),
    #path('main', views.main, name="mainpage_main")
]