#IMPORT DRF SERIALIZERS
from rest_framework import serializers

from api.models import Planta, PlantaData


class PlantaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantaData
        fields = ('id','title', 'description','planta')

class PlantaSerializer(serializers.ModelSerializer):
    planta_data = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Planta
        fields = '__all__'

    def get_planta_data(self,obj):
        try:
            serializer = PlantaDataSerializer(PlantaData.objects.filter(planta__pk=obj.id), many=True)
            return serializer.data
        except PlantaData.DoesNotExist:
            return None