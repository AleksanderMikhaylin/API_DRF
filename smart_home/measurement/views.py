# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer
from measurement.models import Sensor, Measurement


class SensorListView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    # def post(self, request):
    #     return Response({'status': 'OK'})
#
#
#
# class MeasurementView(ListAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorDetailSerializer
#
#     # def post(self, request):
#     #     return Response({'status': 'OK'})
#
#
# class MeasurementSerializerView(RetrieveAPIView):
#     queryset = Measurement.objects.all()
#     serializer_class = MeasurementSerializer
