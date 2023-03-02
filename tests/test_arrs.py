from utils import arrs
import pytest


@pytest.fixture
def test_list_1():
    return [1, 2, 3, 4]


def test_get(test_list_1):
    """тест функции get"""
    assert arrs.get(test_list_1, 1, "test") == 2
    assert arrs.get(test_list_1, 5, "test") == "test"
    assert arrs.get(test_list_1, -1, "test") == "test"


def test_slice(test_list_1):
    """тест функции slice"""
    assert arrs.my_slice(test_list_1, 1, 3) == [2, 3]
    assert arrs.my_slice(test_list_1, 1) == [2, 3, 4]
    assert arrs.my_slice([], 1, 3) == []
    assert arrs.my_slice(test_list_1, -5, 3) == [1, 2, 3]
    assert arrs.my_slice(test_list_1, -2, 4) == [3, 4]
