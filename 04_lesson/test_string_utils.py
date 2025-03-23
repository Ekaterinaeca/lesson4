from string_utils import StringUtils

# Создание объекта класса StringUtils для тестирования
sut = StringUtils()

def test_capitalize_positive():
    assert sut.capitalize("skypro") == "Skypro"

def test_capitalize_empty_string():
    assert sut.capitalize("") == ""

def test_trim_positive():
    assert sut.trim("   skypro") == "skypro"

def test_trim_string_with_space():
    assert sut.trim(" skypro") == "skypro"

def test_trim_empty_string():
    assert sut.trim("") == ""

def test_contains_positive():
    assert sut.contains("SkyPro", "S") == True
    assert sut.contains("SkyPro", "U") == False

def test_contains_empty_string():
    assert sut.contains("", "A") == False

def test_contains_space():
    assert sut.contains("Sky Pro", " ") == True

def test_delete_symbol_positive():
    assert sut.delete_symbol("SkyPro", "k") == "SyPro"
    assert sut.delete_symbol("SkyPro", "Pro") == "Sky"

def test_delete_symbol_not_present():
    assert sut.delete_symbol("SkyPro", "Z") == "SkyPro"

def test_delete_symbol_empty_string():
    assert sut.delete_symbol("", "Z") == ""

def test_delete_symbol_space():
    assert sut.delete_symbol("Sky Pro", " ") == "SkyPro"