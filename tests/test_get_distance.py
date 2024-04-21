import pytest

from get_distance import get_distance


@pytest.fixture
def sample_distance_data():
    """Creates sample distance data for use in the tests."""
    sample_distance_data = [
        [0, "", ""],
        [7.1, 0, ""],
        [6.4, 9.2, 0],
    ]
    return sample_distance_data


def test_get_distance_without_blank(sample_distance_data):
    """Tests the 'get_distance' function for situation where no blank is found in accessing distance matrix."""

    # Initialize sample indices for accessing the data matrix
    address1_index = 1
    address2_index = 0
    # Initialize the expected distance to be returned based on the sample data and selected indices
    expected_distance = 7.1

    # Call the function and assert the result
    assert get_distance(sample_distance_data, address1_index, address2_index) == expected_distance


def test_get_distance_with_blank(sample_distance_data):
    """Tests the 'get_distance' function for situation where a blank is found in accessing distance matrix."""

    # Initialize sample indices for accessing the data matrix with values that will find a blank
    address1_index = 0
    address2_index = 2
    # Initialize the expected distance to be returned based on the sample data and selected indices
    expected_distance = 6.4

    # Call the function and assert the result
    assert get_distance(sample_distance_data, address1_index, address2_index) == expected_distance

