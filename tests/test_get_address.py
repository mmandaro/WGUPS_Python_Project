import pytest

from get_address import get_address


# Use the pytest fixture decorator to create sample address data that can be reused for each test
@pytest.fixture
def address_data():
    """Creates sample address data for testing that can be reused in get_address testing."""
    return [[0, "Location 1 Test", "1234 Test Address 1"],
            [1, "Location 2 Test", "4321 Test Address 2"],
            [2, "Location 3 Test", "2143 Test Address 3"]]


def test_get_address_found(address_data):
    """Test for 'get_address' function to ensure it finds an address that exists and returns its index."""
    # Verify that get_address correctly retrieves and returns the index for the address
    assert get_address("1234 Test Address 1", address_data) == 0


def test_get_address_not_found(address_data):
    """Test that ensures None is returned when address is not in address data."""
    assert get_address("Address That Is Not In Data", address_data) is None


def test_get_address_empty_address_data():
    """Test that ensures None is returned when address data is empty."""
    assert get_address("1234 Test Address 1", []) is None


def test_get_address_data_empty_address_string(address_data):
    """Test that ensures None is returned when the address string is empty."""
    assert get_address("", address_data) is None