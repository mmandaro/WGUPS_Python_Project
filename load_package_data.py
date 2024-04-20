import csv
from package_class import Package


def load_package_data(chaining_hash):
    """Function to load the package data from the csv file."""
    with open("WGUPS_Package_File.csv", 'r') as package_data_file:
        # Uses csv reader to read the package data
        package_data_csv = csv.reader(package_data_file)
        # Makes the package data into a list, so we can iterate over it
        package_data = list(package_data_csv)
        # Removes headers and blanks from the package_data list
        package_data = package_data[2:-7]

        # Iterates through each row of the package data
        for package_row in package_data:
            # Sets the package ID
            package_id = int(package_row[0])
            # Sets the package address
            address = package_row[1]
            # Sets the package city
            city = package_row[2]
            # Sets the package state
            state = package_row[3]
            # Sets the package zipcode
            zipcode = package_row[4]
            # Sets the package deadline
            deadline = package_row[5]
            # Sets the weight of the package
            mass = package_row[6]
            # Initializes package status to 'At Hub'
            status = 'At Hub'

            # Create a package object using the package class and the variables saved above
            package = Package(package_id, address, city, state, zipcode, deadline, mass, status)

            # Insert package into the hashtable, with package_id as the key, and package as the item
            chaining_hash.insert(package_id, package)
