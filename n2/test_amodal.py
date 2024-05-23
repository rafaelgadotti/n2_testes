import pytest

@pytest.mark.amodal
def test_amodal(stat_instance):
    assert stat_instance.amodal([1, 2, 3, 4, 5]) == "Sim"

@pytest.mark.xfail
def test_amodal_fail(stat_instance):
    assert stat_instance.amodal([1, 2, 3]) == "Não"
