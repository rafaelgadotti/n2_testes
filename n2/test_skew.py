import pytest

@pytest.mark.skew
def test_skew(stat_instance):
    assert stat_instance.skew([1, 2, 3, 4, 5]) == 0

@pytest.mark.xfail
def test_skew_fail(stat_instance):
    assert stat_instance.skew([1, 2, 3]) == 1
