import pytest

@pytest.mark.mediana
@pytest.mark.parametrize("lista, expected", [
    ([1, 2, 3, 4, 5], 3),
    ([10, 20, 30, 40, 50], 30)
])
def test_mediana(stat_instance, lista, expected):
    assert stat_instance.mediana(lista) == expected

@pytest.mark.xfail
def test_mediana_fail(stat_instance):
    assert stat_instance.mediana([1, 2, 3]) == 0
