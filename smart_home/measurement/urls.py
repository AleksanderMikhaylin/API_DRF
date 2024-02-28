from django.urls import path

from .views import SensorView


urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<int:pk>/', SensorView.as_view()),
]
