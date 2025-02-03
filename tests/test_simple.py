import pytest

def test_math_addition():
    assert 2 + 2 == 4

def test_string_upper():
    assert "hello".upper() == "HELLO"

def test_list_length():
    assert len([1, 2, 3]) == 3

def test_dict_key():
    d = {"key": "value"}
    assert "key" in d

def test_boolean_true():
    assert True is True

def test_multiplication():
    assert 5 * 5 == 25

def test_float_comparison():
    assert abs(0.1 + 0.2 - 0.3) < 1e-9

def test_math_fail():
    assert 2 + 2 == 5

def test_string_fail():
    assert "pytest".lower() == "Pytest"

def test_list_fail():
    assert len([]) == 1

def test_dict_fail():
    d = {"key": "value"}
    assert "missing_key" in d

def test_boolean_fail():
    assert False is True

@pytest.mark.skip(reason="Фича не реализована")
def test_skipped_feature():
    assert 1 == 1

@pytest.mark.skipif(3 > 2, reason="Условие всегда истинно, тест пропускается")
def test_skipped_condition():
    assert 2 + 2 == 4

@pytest.mark.skip(reason="Временный пропуск")
def test_temp_skipped():
    assert "test" == "test"