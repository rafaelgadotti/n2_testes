from stat_funcs import StatsN2
import pytest

@pytest.fixture
def stat_instance():
    return StatsN2()
