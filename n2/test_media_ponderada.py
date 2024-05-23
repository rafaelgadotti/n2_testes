import pytest

@pytest.mark.media_ponderada
@pytest.mark.parametrize("lista, pesos, expected", [
    ([1, 2, 3], [1, 2, 3], 2),
    ([10, 20, 30], [1, 2, 1], 20)
])
def test_media_ponderada(stat_instance, lista, pesos, expected):
    assert stat_instance.media_ponderada(lista, pesos) == expected

@pytest.mark.xfail
def test_media_ponderada_fail(stat_instance):
    assert stat_instance.media_ponderada([1, 2, 3], [1, 2, 3]) == 0
