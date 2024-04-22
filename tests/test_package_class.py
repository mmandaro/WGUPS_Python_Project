from package_class import Package


def test_package_class():
    """Tests the 'Package' class"""
    # Create a package object
    package = Package(4, "1234 Address St.", "Miami", "Kansas", 92243, 10, "10:30:00", "At Hub")

    # Initialize the expected output for 'package' with the __str__() method
    expected_string = f"Package {package.package_id}:\n" \
                      f"Address: {package.address}, {package.city}, {package.state}, {package.zipcode}\n"\
                      f"Deadline: {package.deadline}, Mass: {package.mass}\n" \
                      f"Status: {package.current_status}, Depart Time: {package.depart_time}, Arrive Time:" \
                      f" {package.arrive_time}\n"
    # Assert that calling the __str__() method on 'package' returns the right string
    assert str(package) == expected_string