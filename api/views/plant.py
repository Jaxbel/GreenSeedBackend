from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Planta, PlantaData
from api.serializers.plant import PlantaDataSerializer, PlantaSerializer


class PlantView(APIView):
    def get(self, request):
        plants = Planta.objects.all()
        serializer = PlantaSerializer(plants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        serializer = PlantaSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message":"Plant saved"}, status=status.HTTP_201_CREATED)
    
class PlantViewDetails(APIView):
    def get(self, request, pk):
        plant = Planta.objects.get(id=pk)
        serializer = PlantaSerializer(plant, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        plant = Planta.objects.get(id=pk)
        serializer = PlantaSerializer(instance=plant, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message":"Plant updated"}, status=status.HTTP_200_OK)

class PlantDataView(APIView):
    def post(self, request):
        data = request.data
        serializer = PlantaDataSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message":"Plant data saved"}, status=status.HTTP_201_CREATED)

class PlantDataViewDetails(APIView):
    
    def put(self, request, pk):
        plant_data = PlantaData.objects.get(id=pk)
        serializer = PlantaDataSerializer(instance=plant_data, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message":"Plant data updated"}, status=status.HTTP_200_OK)