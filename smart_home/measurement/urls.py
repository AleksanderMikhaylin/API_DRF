from django.urls import path

from .views import SensorListView, SensorView


urlpatterns = [
    path('sensors/', SensorListView.as_view()),
    path('sensors/<int:pk>/', SensorView.as_view()),
]
