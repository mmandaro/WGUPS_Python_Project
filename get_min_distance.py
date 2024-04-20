from get_address import get_address
from get_distance import get_distance


def get_min_distance(truck_address, truck_packages, address_data, distance_data, chaining_hashtable):
    """Function that will return the minimum distance from truck's current address to its closest package address."""

    # Initialize min distance to a large number so the if statement will execute at least once
    minimum_distance = 9999

    # Get the index for the trucks current address
    truck_address_index = get_address(truck_address, address_data)

    # Iterate through each package ID in the truck
    for package_id in truck_packages:
        # Assigns package address with the address for the current package ID
        package_address = chaining_hashtable.search(package_id).address

        # Gets the index for the package
        package_index = get_address(package_address, address_data)

        # Get the distance between trucks current location and the package delivery address
        distance = get_distance(distance_data, truck_address_index, package_index)

        # Branch that is taken if a new minimum distance is found
        if distance <= minimum_distance:
            # Keep the address for the minimum distance package
            package_address_final = package_address

            # Overwrite minimum distance so that the true minimum is kept
            minimum_distance = distance

            # Package ID for the minimum distance package
            package_id_min = package_id

    # Returns list with package & address info including the distance from truck's current address to next address
    return [package_id_min, package_address_final, minimum_distance]
