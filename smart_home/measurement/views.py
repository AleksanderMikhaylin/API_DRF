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


class SensorView(APIView):

    def get(self, request, pk):
        if not pk.isdigit():
            return Response({'err': 'Не верный id датчика'})

        sensors = Sensor.objects.filter(id=int(pk))
        serializer = SensorDetailSerializer(sensors, many=True)
        return Response({"articles": serializer.data})

    def post(self, request, pk):
        if not pk.isdigit():
            return Response({'err': 'Не верный id датчика'})

        sensors = Sensor.objects.filter(id=int(pk))
        if sensors is None:
            return Response({f'err': f'Датчик с id={pk} не существует!'})

        temperature = request.data.get("temperature")
        if temperature is None:
            return Response({'err': 'Не найден параметр температуры'})
        if not temperature.isdigit():
            return Response({'err': 'Не верный параметр температуры'})

        serializer = MeasurementSerializer(data=dict(sensor_id=pk, temperature=temperature, created_at=datetime.now()))
        if serializer.is_valid(raise_exception=True):
            sensor_saved = serializer.save()
            return Response({"success": f"Показания температуры {sensor_saved.temperature}C для датчика '{sensors.name}' добавлены успешно"})
        return Response({'err': f'Ошибка добавления показания для датчика {sensors.name}'})

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

