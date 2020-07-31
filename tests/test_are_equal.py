from pygeo import are_equal
import pytest

#we have to give the test a proper name such as demonstraed
#test__unit_of_work__state_under_test__expected_behaviour

def test__given_two_equal_numbers__returns_true():
    assert are_equal(0.1+0.2 , 0.3) is True


def test__given_two_equal_numbers__returns_false():
    assert are_equal(0.1+0.2 , 0.4) is False


def test__given_two_unequal_numbers__returns_False():
    assert are_equal(0.1+0.2 , 0.2) is False


def test__given_two_equal_integer__returns_True():
    assert are_equal(1 + 2 , 3) is True


def test_given_two_uneual_integer__returns_False():
    assert are_equal( 1 + 2 , 4) is False


def test__given_two_unequal_integer_returns_False():
    assert are_equal( 1 + 2 , 2) is False


def test__given_two__unequal_small_numbers__returns_false():
    assert are_equal( 1e-9 + 2e-9 , 4e-9,tolerance=1e-17) is False


def test__given_two_very_large_unequal_number_returns_false():
    assert are_equal( 1e9 + 2e9 , 4e9) is False


def test__given_two_very_large_numbers__returns_true():
    """Assume we hardcore a tolerance , it might be too small."""
    assert are_equal( 1e23 + 2e23 , 3e23,tolerance=1e15) is True

def test_given_negative_tolerance_raise_ValueError():
    with pytest.raises(ValueError):
        are_equal(0.1+0.2,0.3,tolerance=-1e2)