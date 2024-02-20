from django.urls import path

from .views import SensorListView, SensorView


urlpatterns = [
    path('list_sensor/', SensorListView.as_view()),
    path('sensor/<pk>/', SensorView.as_view()),
]