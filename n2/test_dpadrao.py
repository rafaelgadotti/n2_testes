import pytest

@pytest.mark.dpadrao
@pytest.mark.parametrize("var, expected", [
    (2.5, 1.5811388300841898),
    (250, 15.811388300841896)
])
def test_dpadrao(stat_instance, var, expected):
    assert stat_instance.dpadrao(var) == expected

@pytest.mark.xfail
def test_dpadrao_fail(stat_instance):
    assert stat_instance.dpadrao(2.5) == 0
