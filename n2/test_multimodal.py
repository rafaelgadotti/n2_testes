import pytest

@pytest.mark.multimodal
def test_multimodal(stat_instance):
    assert stat_instance.multimodal([1, 2, 3, 4, 5]) == "Sim"

@pytest.mark.xfail
def test_multimodal_fail(stat_instance):
    assert stat_instance.multimodal([1, 2, 3]) == "Não"
