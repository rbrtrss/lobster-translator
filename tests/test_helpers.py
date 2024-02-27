from lobster_translator.helpers import get_interaction_from_line

INTERACTION_LINE="No.5:P57->P52(2.2406954043362486)"

def test_get_interaction_from_line():
    assert get_interaction_from_line(INTERACTION_LINE) == "P57P52"