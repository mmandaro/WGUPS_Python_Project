from getDistance import get_distance
from get_min_distance import get_min_distance
from getAddress import get_address
import datetime


def deliver_package(truck, chaining_hash_table, address_data, distance_data):
    """Function that uses the nearest neighbor algorithm to determine the trucks delivery route."""

    # Initialize a variable that will track the total time for deliveries
    time_sum = truck.depart_time

    # Initialize the current address to the trucks starting address
    current_address = truck.address

    # Update the packages that are on the truck to en route and set their depart time to the trucks depart time
    for item in truck.packages:
        chaining_hash_table.search(item).current_status = "En Route"
        chaining_hash_table.search(item).depart_time = truck.depart_time

    # Iterates so long as there are packages on the truck
    while (len(truck.packages)) > 0:

        # Finds the closest destination using nearest neighbor algorithm
        min_distance_list = get_min_distance(current_address, truck.packages, address_data, distance_data,
                                             chaining_hash_table)

        # The package ID of the nearest address from the list above
        next_address_ID = min_distance_list[0]

        # The string address of the nearest address from the list above
        next_address = min_distance_list[1]

        # The actual distance from current address to next address
        distance_to_next = min_distance_list[2]

        # Add the miles traveled to next address to total truck mileage
        truck.mileage += distance_to_next

        # How long it takes to get from current address to next
        time_to_deliver = datetime.timedelta(hours=(distance_to_next / truck.speed))

        # Keeps track of total time
        time_sum += time_to_deliver

        # Updates arrival time for the package
        chaining_hash_table.search(next_address_ID).arrive_time = time_sum

        # updates delivery status for package
        chaining_hash_table.search(next_address_ID).current_status = 'Delivered'

        # Remove the package from the truck list, as it is delivered
        truck.packages.remove(next_address_ID)

        if len(truck.packages) > 1:
            # Now that package has been delivered, update current address
            current_address = next_address

    # Gets hubs address index, so we can get the distance
    hub_address_index = get_address(truck.address, address_data)

    # Gets the current address index
    current_address_index = get_address(current_address, address_data)

    # get the distance to return to hub
    distance_to_hub = get_distance(distance_data, current_address_index, hub_address_index)

    # Return truck to hub and update miles
    truck.mileage += distance_to_hub

    # Getting the time the truck is back at hub
    time_sum += datetime.timedelta(hours=(distance_to_hub / truck.speed))

    # Returning the time the truck gets back to the hub
    return time_sum
