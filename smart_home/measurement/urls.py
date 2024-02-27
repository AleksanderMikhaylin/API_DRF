from django.urls import path

from .views import SensorListView, SensorView


urlpatterns = [
    path('list_sensor/', SensorListView.as_view()),
    path('add_sensor/', SensorAdd.as_view()),
    path('sensor/<int:pk>/', SensorView.as_view()),
]
