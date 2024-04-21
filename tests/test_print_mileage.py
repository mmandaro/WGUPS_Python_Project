from io import StringIO
import sys
from truck_class import Truck
from print_mileage import print_mileage


def test_print_mileage():
    """Tests the output of print_mileage."""
    # Initialize 3 truck objects with mileage
    truck1 = Truck("", 100, "", "")
    truck2 = Truck("", 200, "", "")
    truck3 = Truck("", 10, "", "")

    # Create a variable with the expected output of 'print_mileage'
    expected_output = f"""\
Truck 1 Mileage: {truck1.mileage}
Truck 2 Mileage: {truck2.mileage}
Truck 3 Mileage: { truck3.mileage}
TOTAL MILEAGE: {(truck1.mileage + truck2.mileage + truck3.mileage)}\n
"""
    # Capture the printed output
    captured_output = StringIO()
    sys.stdout = captured_output

    # Call the function 'print_mileage'
    print_mileage(truck1, truck2, truck3)

    # Save the printed output
    printed_output = captured_output.getvalue()

    # Assert that the saved output matches the expected
    assert printed_output == expected_output

    # Reset the standard output
    sys.stdout = sys.__stdout__

