from lobster_translator.helpers import get_interaction_from_line
from lobster_translator.helpers import get_indicator_from_path

INTERACTION_LINE="No.5:P57->P52(2.2406954043362486)"

def test_get_interaction_from_line():
    assert get_interaction_from_line(INTERACTION_LINE) == "P57P52"



PROPERTY_PATH="/foo/bar/structure//ICOBILIST.lobster"
SHORT_PATH="ICOOPLIST.lobster"

def test_get_indicator_from_path():
    assert get_indicator_from_path(PROPERTY_PATH) == "icobi"

def test_get_indicator_from_path_short():
    assert get_indicator_from_path(SHORT_PATH) == "icoop"
