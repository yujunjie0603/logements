import pytest
from gestion_logement.models import Appartment

@pytest.fixture
def appartement_data():
    return {
        "name": "Appartement Test",
        "floor": 2,
        "number": 101,
        "address": "123 Rue Exemple",
        "city": "Paris",
        "cp": "75001",
        "country": "France",
        "type": "APP",
    }


@pytest.fixture
def create_appartement(db, appartement_data):
    return Appartment.objects.create(**appartement_data)


@pytest.mark.django_db
def test_model_creation():
    obj = Appartment.objects.create(name='Test', number=1)
    assert obj.name == 'Test'

def test_appartement_creation(create_appartement):
    app = Appartment.objects.get(name="Appartement Test")

    assert create_appartement.name == "Appartement Test"
    assert create_appartement.floor == 2
