import pytest

@pytest.mark.unimodal
def test_unimodal(stat_instance):
    assert stat_instance.unimodal([1, 2, 3, 4, 5]) == "Sim"

@pytest.mark.xfail
def test_unimodal_fail(stat_instance):
    assert stat_instance.unimodal([1, 2, 3]) == "Não"
