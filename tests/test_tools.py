
import pytest
from tools import data_tools as dt

@pytest.fixture
def get_df():
    df = dt.load_square_drives()
    return df


def test_filter_nb_menages(get_df):
    df = get_df
    nbHab_min = 20.0 
    nbHab_max = float(df.Nb_menages.max())
    chosen_nbHab_min = 20
    df = df[ df['Nb_menages'] >= chosen_nbHab_min ]
    assert df.iloc[1]['Nb_menages'] >= chosen_nbHab_min


def test_filter_score(get_df):
    df = get_df
    score_min = float(df.Score.min())
    score_max = float(df.Score.max())
    chosen_score_min = 0.5
    df = df[ df['Score'] >= chosen_score_min ]
    assert df.iloc[1]['Score'] >= chosen_score_min



