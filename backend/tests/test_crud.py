import pytest
from gestion_logement.models import Appartment

@pytest.mark.django_db
def test_model_creation():
    obj = Appartment.objects.create(name='Test', number=1)
    assert obj.name == 'Test'