from truck_class import Truck


def test_truck_class():
    """Tests the Truck class."""

    # Initialize a truck object
    truck = Truck("0900", 0, [], "1234 Address")

    # Create the expected output of the '__str__()' method on the truck object
    expected_string = f"Depart Time: {truck.depart_time}, Mileage: {truck.mileage}, Packages: {truck.packages}"\
                      f"Address: {truck.address}, Carry Max: {truck.carry_max,}, Speed: {truck.speed}"

    # Assert that 'str(truck)' is equal to 'expected_string'
    assert str(truck) == expected_string