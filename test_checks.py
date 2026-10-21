import pytest
from Checks import (length_check, num_specials, num_uppers,
                     predictable_dates_check, common_pattern_check,
                     common_password_check)
@pytest.mark.xfail(strict=True, reason="Date range is hardcoded and misses the current year") -- this is my first time using pytest so I wanted to make sure it didn't just pass every test
def test_length_check_boundaries():
    assert length_check("abc") == 0
    assert length_check("a" * 8) == 1
    assert length_check("a" * 12) == 2  
    assert length_check("a" * 16) == 3

def test_num_specials():
    assert num_specials("a!b@") == 2
    assert num_specials("abc") == 0

def test_num_uppers():
    assert num_uppers("AbC") == 2

def test_predictable_dates():
    assert predictable_dates_check("pass1999") == 0
    assert predictable_dates_check("password") == 3

def test_keyboard_patterns():
    assert common_pattern_check("myqwertypass") == 0
    assert common_pattern_check("xk9vq2") == 3

def test_common_password():
    assert common_password_check("password") == 0