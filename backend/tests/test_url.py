import pytest
from unittest.mock import patch, MagicMock
from django.test import Client
from django.urls import reverse
from rest_framework.test import APIClient

@pytest.mark.django_db
@patch("gestion_logement.views.Appartment.objects.all")
def test_list_appartements_with_mock(mock_all):
    
    fake_appartment = MagicMock()
    fake_appartment.name = "MockApp"
    fake_appartment.address = "MockAddress"
    
    mock_all.return_value = [fake_appartment]
    
    client = APIClient()
    
    response = client.get("/gestion_logement/appartment/")
    url = reverse('appartment-list')
    
    assert response.status_code == 200
    
    