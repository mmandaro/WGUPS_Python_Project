# a function that will use the nearest neighbor algorithm to determine the trucks delivery route

from getDistance import getdistance
from get_min_distance import get_min_distance
from getAddress import getaddress
import datetime

def deliver_package(truck, chaining_hash_table, addressdata, distancedata):
    time_sum = truck.depart_time  # initialize a variable that will track the total time for deliveries

    current_address = truck.address  # initialize the current address to the trucks starting address

    # update the packages that are on the truck to en route and set their depart time to the trucks depart time
    for item in truck.packages:
        chaining_hash_table.search(item).current_status = "En Route"
        chaining_hash_table.search(item).depart_time = truck.depart_time

    while (len(truck.packages)) > 0:  # iterates so long as there are packages on the truck
        # finds the closest destination using nearest neighbor algorithm
        min_distance_list = get_min_distance(current_address, truck.packages, addressdata, distancedata,
                                        chaining_hash_table)  # gets the ID, address, and distance to nearest address

        next_address_ID = min_distance_list[0]  # the package ID of the nearest address from the list above

        next_address = min_distance_list[1]  # the string address of the nearest address from the list above

        distance_to_next = min_distance_list[2]  # the actual distance from current address to next address

        truck.mileage += distance_to_next  # add the miles traveled to next address to total truck mileage

        # how long it takes to get from current address to next
        time_to_deliver = datetime.timedelta(hours=(distance_to_next / truck.speed))

        time_sum += time_to_deliver  # keeps track of total time
        chaining_hash_table.search(next_address_ID).arrive_time = time_sum  # updates arrival time for the package

        chaining_hash_table.search(next_address_ID).current_status = 'Delivered'  # updates delivery status for package

        truck.packages.remove(next_address_ID)  # remove the package from the truck list, as it is delivered

        if len(truck.packages) > 1:
            current_address = next_address  # now that package has been delivered, update current address

    hub_address_index = getaddress(truck.address, addressdata)  # gets the hubs address index so we can get the distance

    current_address_index = getaddress(current_address, addressdata)  # gets the current address index
    # get the distance to return to hub
    distance_to_hub = getdistance(distancedata, current_address_index, hub_address_index)

    truck.mileage += distance_to_hub # return truck to hub and update miles

    time_sum += datetime.timedelta(hours=(distance_to_hub / truck.speed))  # getting the time the truck is back at hub

    return time_sum  # returning the time the truck gets back to the hub




