# define a function that will return the minimum distance from trucks current address to its package addresses
from getAddress import getaddress
from getDistance import getdistance

def get_min_distance(truck_address, truck_packages, addressdata, distancedata, chaining_hashtable):
    minimum_distance = 9999  # initialize min distance to a large number so the if statement will execute at least once

    truck_address_index = getaddress(truck_address, addressdata)  # get the index for the trucks current address


    for package_id in truck_packages:  # iterate through each package ID in the truck
        # assigns package address with the address for the package ID
        package_address = chaining_hashtable.search(package_id).address

        package_index = getaddress(package_address, addressdata)  # gets the index for the package

        # get the distance between trucks current location and the package delivery address
        distance = getdistance(distancedata, truck_address_index, package_index)


        if distance <= minimum_distance:  # if branch that is taken if a new minimum distance is found
            package_address_final = package_address  # keep the address for the minimum distance package

            minimum_distance = distance  # overwrite minimum distance so that the true minimum is kept

            package_id_min = package_id  # package ID for the minimum distance package

    return [package_id_min, package_address_final, minimum_distance]  # returns a list with the address ID/ address
    # that's min distance away and the distance to that address from the trucks current address
