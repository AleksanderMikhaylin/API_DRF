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

    def post(self, request):

        print(request)
        name = request.data.get("name")
        description = request.data.get("description")
        if name is None:
            return Response({'err': 'Не верное название датчика'})

        return Response({"success": f"Sensor '{name}' создан успешно"})
