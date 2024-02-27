# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer, CreateMeasurementSerializer
from measurement.models import Sensor, Measurement
from datetime import datetime


class SensorListView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorView(APIView):

    def get(self, request, pk):

        sensors = Sensor.objects.filter(id=int(pk))
        serializer = SensorDetailSerializer(sensors, many=True)
        return Response({"sensor": serializer.data})

    def post(self, request, pk):

        sensor = Sensor.objects.filter(id=int(pk)).first()
        if sensor is None:
            return Response({f'err': f'Датчик с id={pk} не существует!'})

        temperature = request.data.get("temperature")
        if temperature is None:
            return Response({'err': 'Не найден параметр температуры'})
        try:
            temperature_float = float(temperature)
        except:
            return Response({'err': 'Не верный параметр температуры'})

        data = {
            'sensor_id': int(pk),
            'temperature': '{:.1f}'.format(temperature_float),
            'created_at': datetime.now(),
        }

        # serializer = MeasurementSerializer(data=data)
        serializer = CreateMeasurementSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            sensor_saved = serializer.save()
            return Response({"success": f"Показания температуры {sensor_saved.temperature}C для датчика '{sensor.name}' добавлены успешно"})
        return Response({'err': f'Ошибка добавления показания для датчика {sensor.name}'})
