from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from gestion_logement.models import Appartment, Building, Photo
from gestion_logement.serializers import AppartmentSerializer, BuildingSerializer, PhotoSerializer


# Create your views here.
def index(request):
    return HttpResponse("Hello logement")

class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    
class AppartementViewSet(viewsets.ModelViewSet):
    queryset = Appartment.objects.all()
    serializer_class = AppartmentSerializer
    
class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer