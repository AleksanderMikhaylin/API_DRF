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

class SensorAdd(APIView):

    def get(self, request):
        return Response({"err": "Method 'GET' not allowed."})

    def post(self, request):

        # print(request)
        name = request.data.get("name")
        description = request.data.get("description")
        if name is None:
            return Response({'err': 'Не верное название датчика'})

        serializer = SensorSerializer(data=dict(name=name, description=description))
        if serializer.is_valid(raise_exception=True):
            sensor_saved = serializer.save()
            return Response({"success": f"Sensor '{sensor_saved.name}' создан успешно, id={sensor_saved.id}"})
        return Response({'err': 'Ошибка создания датчика'})

