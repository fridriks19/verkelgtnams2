from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="computers-index"),
    path('<int:id>', views.get_computers_by_id, name="computers_details")
]