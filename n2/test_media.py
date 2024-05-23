import pytest

@pytest.mark.media
@pytest.mark.parametrize("lista, expected", [
    ([1, 2, 3, 4, 5], 3),
    ([10, 20, 30, 40, 50], 30)
])
def test_media(stat_instance, lista, expected):
    assert stat_instance.media(lista) == expected

@pytest.mark.xfail
def test_media_fail(stat_instance):
    assert stat_instance.media([1, 2, 3]) == 0
