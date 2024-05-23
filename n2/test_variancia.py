import pytest

@pytest.mark.variancia
@pytest.mark.parametrize("lista, expected", [
    ([1, 2, 3, 4, 5], 2.5),
    ([10, 20, 30, 40, 50], 250)
])
def test_variancia(stat_instance, lista, expected):
    assert stat_instance.variancia(lista) == expected

@pytest.mark.xfail
def test_variancia_fail(stat_instance):
    assert stat_instance.variancia([1, 2, 3]) == 0
