import datetime
from package_class import Package
from load_package_data import load_package_data
from load_distance_data import load_distance_data
from load_address_data import load_address_data
from hashtable import ChainingHashTable
from truck_class import Truck
from deliver_package import deliver_package
from display_user_interface import display_user_interface
from print_mileage import print_mileage
from get_next_input import get_next_input


# Initialize a chaining hash table
package_hash = ChainingHashTable()

# Use 'load_package_data' function with the empty hashmap as input to put package data into the hashmap
load_package_data(package_hash)

# Use 'load_distance_data' to get the distance information and assign it to a variable
distance_data = load_distance_data()

# Use 'load_address_data' to get the addresses and assign them to a variable
address_data = load_address_data()

# Create the truck objects and set them with their respective initial conditions
truck1 = Truck(datetime.timedelta(hours=8), 0, [], '4001 South 700 East')
# Load the truck based on given constraints
truck1.packages = [1, 13, 14, 15, 16, 19, 20, 21, 29, 30, 31, 34, 37, 40]

truck2 = Truck(datetime.timedelta(hours=9, minutes=5), 0, [], '4001 South 700 East')
truck2.packages = [2, 3, 4, 5, 6, 7, 8, 10, 11, 17, 18, 25, 26, 28, 36, 38]

# Driver 1 switches from truck 1 to truck 3 after delivering truck 1's packages. Truck 1 is finished at 10:19 am
truck3 = Truck(datetime.timedelta(hours=10, minutes=20), 0, [], '4001 South 700 East')
# Update package 9's address after 10:20 am as per project requirements
updated_package9 = Package(9, "410 S State St", "Salt Lake City", "UT", 84111, "EOD", package_hash.search(9).mass,
                           "At Hub")
# Insert and replace the original package 9 info with updated version
package_hash.insert(9, updated_package9)
# load the truck based on the given constraints
truck3.packages = [9, 12, 22, 23, 24, 27, 32, 33, 35, 39]

# Deliver truck 1's packages and save the ending time
end_time_truck1 = deliver_package(truck1, package_hash, address_data, distance_data)
# Deliver truck 2's packages and save the ending time
end_time_truck2 = deliver_package(truck2, package_hash, address_data, distance_data)
# Deliver truck 3's packages and save the ending time
end_time_truck3 = deliver_package(truck3, package_hash, address_data, distance_data)

# Display the user interface
display_user_interface()

# Gets the users input
user_choice = int(input("Input: "))

# Branch for invalid input
if (user_choice < 1) or (user_choice > 4):
    # Prints out error message for invalid input
    print("Invalid Entry, Please Try Again")
    # Takes in a new user input
    user_choice = int(input("Input: "))
    # Repeats the above so long as an invalid input is received
    while (user_choice < 1) or (user_choice > 4):
        print("Invalid Entry, Please Try Again")
        user_choice = int(input("Input: "))

# Loops until the user selects 4 for exit
while user_choice != 4:

    # Branch for user selection 1, prints all package status and truck mileage
    if user_choice == 1:
        # Creates a loop that will iterate from 1 to 40, representing the package ID's
        for i in range(1, 41):
            # Each pass of the loop will access the package object from the hash table
            package = package_hash.search(i)
            # Prints the package information
            print(package)
        # Prints the individual trucks mileage as well as the total mileage
        print_mileage(truck1, truck2, truck3)

        # Gets new user input after the above loop is complete
        user_choice = get_next_input()

    # Branch for user choice number 2, allowing a single package to be selected for given time
    elif user_choice == 2:
        # Gets user input of package ID to look up
        user_choice_package = int(input("Enter the package ID for the package: "))

        # Branches only if a valid ID is input
        if 1 <= user_choice_package <= 40:
            # Asks user for time desired to check status of the chosen package
            user_choice_time_input = input("Enter the time to check (use format HH:MM:SS), ")

            # Use 'datetime' built in 'strptime' to convert the input string to a time object
            user_choice_time = datetime.datetime.strptime(user_choice_time_input, "%H:%M:%S")
            # Convert 'user_choice_time' to a time delta for comparison to arrival and departure times
            user_timedelta = datetime.timedelta(hours=user_choice_time.hour, minutes=user_choice_time.minute,
                                                seconds=user_choice_time.second)
            # Looks up the user selected package
            chosen_package = package_hash.search(user_choice_package)

            # If the arrival time of the package is less than the users input time, then the package has arrived
            if chosen_package.arrive_time <= user_timedelta:
                chosen_package.current_status = "Delivered"
                print(chosen_package)
                # Gets the next input from the user
                user_choice = get_next_input()

            # If the arrival time is greater than the users input time, the package could be en route or at hub
            elif chosen_package.arrive_time > user_timedelta:
                # If the departure time is less than or equal to user input time, the package is en route
                if chosen_package.depart_time <= user_timedelta:
                    chosen_package.current_status = "En Route"
                    print(chosen_package)
                    # Gets the next input from the user
                    user_choice = get_next_input()

                # If the departure time is greater than the user input time, the package is still at the hub
                elif chosen_package.depart_time > user_timedelta:
                    chosen_package.current_status = "At Hub"
                    print(chosen_package)
                    # Gets the next input from the user
                    user_choice = get_next_input()

        # If invalid package ID
        else:
            # Loops as long as ID is invalid and gets new ID
            while user_choice_package < 1 or user_choice_package > 40:
                print("Invalid package ID")
                user_choice_package = int(input("Enter the package ID for the package: "))

    elif user_choice == 3:
        # Asks user for desired time
        user_choice_time_input = input("Enter the time to check (use format HH:MM:SS), ")
        # use 'datetime' built in 'strptime' to convert the input string to a time object
        user_choice_time = datetime.datetime.strptime(user_choice_time_input, "%H:%M:%S")
        # Convert the user's selected time to a timedelta
        user_timedelta = datetime.timedelta(hours=user_choice_time.hour, minutes=user_choice_time.minute,
                                            seconds=user_choice_time.second)

        # Creates a loop that will iterate from 1 to 40, representing the package ID's
        for i in range(1, 41):
            # Each pass of the loop will access the package object from the hash table
            package = package_hash.search(i)

            # If the arrival time of the package is less than the users input time, then the package has arrived
            if package.arrive_time <= user_timedelta:
                package.current_status = "Delivered"
                print(package)

            # If the arrival time is greater than the users input time, the package could be en route or at hub
            elif package.arrive_time > user_timedelta:
                # If the departure time is less than or equal to user input time, the package is en route
                if package.depart_time <= user_timedelta:
                    package.current_status = "En Route"
                    print(package)

                # if the departure time is greater than the user input time, the package is still at the hub
                elif package.depart_time > user_timedelta:
                    package.current_status = "At Hub"
                    print(package)

        # Gets the next input from the user
        user_choice = get_next_input()