from display_user_interface import display_user_interface
from io import StringIO
import sys


def test_display_user_interface(capsys):
    """Tests that the display user interface function works as intended."""
    # Store the desired output from 'display_user_interface' in a variable
    expected_output = """\
*****************************************
Welcome to WGUPS Package Delivery Tracker
Please Select An Option:
Press 1 to Check All Package Status and Total Truck Mileage
Press 2 to Get a Single Package Status With a Time
Press 3 to Get All Package Status With a Time
Press 4 to Exit
*****************************************
"""

    # Capture the printed output
    captured_output = StringIO()
    sys.stdout = captured_output

    # Call the function 'display_user_interface'
    display_user_interface()

    # Get the printed output
    printed_output = captured_output.getvalue()

    # Assert that the output matches the expected output
    assert printed_output == expected_output

    # Reset the standard output
    sys.stdout = sys.__stdout__
