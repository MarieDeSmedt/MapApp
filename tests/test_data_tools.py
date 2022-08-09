import pytest
from conftests import *
from tools.data_tools import *






T   
# @pytest.mark.parametrize('territories_json, chosen_territory_name, lat_expected,lon_expected',get_territory_data())
def test_get_territory_lat_lon(get_territory_data):
    # with pytest.raises(AssertionError):
    for data in get_territory_data:
        for territory in data[0]['territory']:
            if territory['territoryLabel'] == data[1]:
                latitude = territory['latitude']
                longitude = territory['longitude']
        assert latitude == data[2]
        assert longitude== data[3]
