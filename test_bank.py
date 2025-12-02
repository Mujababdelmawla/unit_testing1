import pytest
from bank import withdraw

def test_withdraw_valid_amount():
    assert withdraw(100, 200) ==100 

def test_withdraw_exact_amount():
    assert withdraw(500, 500) == 0

def test_withdraw_insuffecient_funds():
    with pytest.raises(ValueError):
        withdraw(200, 100)