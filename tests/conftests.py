import json
import values as val
import pytest

TERRITORY_JSON = json.loads(val.territory_list)

@pytest.fixture
def get_territory_data():
    return [(TERRITORY_JSON,"EST",48.69586941510869,5.60984605583475),(TERRITORY_JSON,"ILE-DE-FRANCE",48.73474076615772,2.4805003703964954)]
 