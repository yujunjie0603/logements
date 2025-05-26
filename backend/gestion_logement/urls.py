from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'appartment', views.AppartementViewSet)
router.register(r'building', views.BuildingViewSet)
router.register(r'photos', views.PhotoViewSet)

urlpatterns = [
    #path('', views.index, name= 'index')
    path('', include(router.urls))
]
