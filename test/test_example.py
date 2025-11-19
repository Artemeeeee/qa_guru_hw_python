import pytest
from cffi.model import voidp_type


@pytest.mark.first
def test_first():
    assert "hello" in "hello world"


@pytest.mark.second
def test_swcond():
    assert len("hello") == 5




