import pytest
import json
import values as val
from tools.data_tools import *

territory_list = json.dumps(val.territories)
TERRITORY_JSON = json.loads(territory_list)

@pytest.fixture
def get_territory_data():
    return [(TERRITORY_JSON,"EST",48.69586941510869,5.60984605583475),(TERRITORY_JSON,"ILE-DE-FRANCE",48.73474076615772,2.4805003703964954)]



def test_get_territory_lat_lon(get_territory_data):
    # with pytest.raises(AssertionError):
    for data in get_territory_data:
        for territory in data[0]['territory']:
            if territory['territoryLabel'] == data[1]:
                latitude = territory['latitude']
                longitude = territory['longitude']
        assert latitude == data[2]
        assert longitude== data[3]


a ="Une bonne couverture de test, supérieure à 80%, est signe d'un projet bien testé et auquel il est plus facile d'ajouter de nouvelles fonctionnalités."

b = "pytest --cov=mapapp  tests/"