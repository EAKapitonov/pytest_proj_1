from utils import dicts
import pytest


@pytest.fixture
def test_dict_1():  # фикстура для тестов
    return {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f"}


@pytest.fixture
def test_dict_0():  # фикстура для теста - пустой словарь
    return {}


def test_get_val(test_dict_1, test_dict_0):
    """тесты для функции get_val"""
    assert dicts.get_val(test_dict_1, 1) == "a"  # вывод значения по ключу, в функцию передается 2 переменных
    assert dicts.get_val(test_dict_1, 1, 'git') == "a"  # вывод значения по ключу, в функцию передается 3 переменых
    assert dicts.get_val(test_dict_0, 1, 'git') == "git"  # вывод в случае пустого словаря
    assert dicts.get_val(test_dict_1, 8, 'bazaar') == "bazaar"  # вывод в случае отсутствие ключа
