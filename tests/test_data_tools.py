import pytest
import json
from tools import data_tools as dt


territories = {
    'territory' : [
  {
    "territoryLabel": "EST",
    "longitude": 5.60984605583475,
    "latitude": 48.69586941510869
  }]}
territory_list = json.dumps(territories)
TERRITORY_JSON = json.loads(territory_list)

@pytest.fixture
def get_territory_data():
    return [(TERRITORY_JSON,"EST",48.69586941510869,5.60984605583475),(TERRITORY_JSON,"ILE-DE-FRANCE",48.73474076615772,2.4805003703964954)]

@pytest.fixture
def get_site():
    choosen_site =['AUCHAN DRIVE']
    return choosen_site

@pytest.fixture
def get_territorylabel():
    choosen_territorylabel = 'EST'
    return choosen_territorylabel


def test_get_territory_lat_lon(get_territory_data):
    for data in get_territory_data:
        for territory in data[0]['territory']:
            latitude1, longitude1 = dt.get_territory_lat_lon(territory['territoryLabel'], TERRITORY_JSON)
            if territory['territoryLabel'] == data[1]:
                latitude2 = territory['latitude']
                longitude2 = territory['longitude']
        assert latitude1 == latitude2
        assert longitude1 == longitude2


def test_get_drives(get_site,get_territorylabel):
    data = dt.get_drives(get_site,get_territorylabel)
    assert( data.iloc[1]['territoryLabel'] == 'EST')
    assert( data.iloc[1]['nom_enseigne'] == 'AUCHAN DRIVE')

def test_get_square_drives(get_territorylabel):
    data = dt.get_square_drives(get_territorylabel)
    assert( data.iloc[1]['territoryLabel'] == 'EST')
    
