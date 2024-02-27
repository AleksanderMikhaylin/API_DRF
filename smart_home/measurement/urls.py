from django.urls import path

from .views import SensorListView, SensorView, SensorAdd


urlpatterns = [
    path('sensor/', SensorAdd.as_view()),
    path('sensors/', SensorListView.as_view()),
    path('sensors/<int:pk>/', SensorView.as_view()),
]
