from string_utils import StringUtils

utils = StringUtils()


def test_capitalize_positive():
    assert utils.capitalize("skypro") == "Skypro"
    assert utils.capitalize("123") == "123"
    assert utils.capitalize("04 апреля 2023") == "04 апреля 2023"


def test_capitalize_negative():
    # БАГ 1: Функция падает с ошибкой, если передать None
    assert utils.capitalize(None) == ""
    assert utils.capitalize("") == ""
    assert utils.capitalize(" ") == " "


def test_trim_positive():
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("skypro") == "skypro"
    assert utils.trim("   skypro   ") == "skypro   "


def test_trim_negative():
    # БАГ 2: Функция падает с ошибкой AttributeError, если передать None
    assert utils.trim(None) == ""
    assert utils.trim("") == ""
    assert utils.trim(" ") == ""


def test_contains_positive():
    assert utils.contains("SkyPro", "S") is True
    assert utils.contains("SkyPro", "U") is False
    assert utils.contains("123", "2") is True


def test_contains_negative():
    # БАГ 3: Функция падает с TypeError, если передать None
    assert utils.contains(None, "S") is False
    assert utils.contains("", "S") is False
    assert utils.contains(" ", " ") is True


def test_delete_symbol_positive():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"
    assert utils.delete_symbol("123", "2") == "13"


def test_delete_symbol_negative():
    # БАГ 4: Функция падает с TypeError, если передать None
    assert utils.delete_symbol(None, "S") == ""
    assert utils.delete_symbol("", "S") == ""
    assert utils.delete_symbol(" ", " ") == ""
