from rest_framework import serializers
from logement import settings
from gestion_logement.models import Appartment, Building, Photo

class BuildingSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Building
        fields = ('name', 'address', 'city', 'country', 'photo')

class AppartmentSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Appartment
        fields = ('name', 'floor', 'number', 'address', 'city', 'country', 'type', 'photo')
        
class PhotoSerializer(serializers.Serializer):
    
    name = serializers.CharField(max_length=100)
    image = serializers.ImageField(allow_empty_file=False)
    
    def create(self, validated_data):
        return Photo.objects.create(**validated_data)