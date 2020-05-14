from django.urls import path
from . import views
urlpatterns = [
    path('get_computers_by_highest', views.get_computers_by_highest, name="computers_highest"),
    path('get_computers_by_lowest', views.get_computers_by_lowest, name="computers_lowest"),
    path('get_computers_by_name', views.get_computers_by_name, name="computers_name"),
    path('', views.index, name="computers-index"),
    path('<int:id>', views.get_computers_by_id, name="computers_details"),
]