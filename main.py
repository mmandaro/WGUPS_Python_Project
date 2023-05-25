# Project By: Morgan Mandaro
# Student ID: 010763397

# import the python datetime module to track the departure and arrival times of packages
# I learned how to use datetime module from https://docs.python.org/3/library/datetime.html
# the above reference and others in this code appear in the typed report's reference page
import datetime
from package_class import Package
from loadPackageData import loadpackagedata  # Imports the loadpackage data function so we can use it on this file
from loadDistanceData import loaddistancedata  # Import the loaddistancedata function to load in the distance info
from loadAddressData import loadaddressdata  # Import the loadaddressdata function to load in the address information
from hashtable import ChainingHashTable  # Import the chaining hash table from hashtable file
from truck_class import Truck  # Import the truck class for use on this file
from deliver_package import deliver_package

packageHash = ChainingHashTable()  # Initialize a chaining hash table

# Use loadpackagedata function with the empty hashmap as input to put package data into the hashmap
loadpackagedata(packageHash)

# use loaddistancedata to get the distance information and assign it to a variable
distance_data = loaddistancedata()

# use loadaddressdata to get the addresses and assign them to a variable
address_data = loadaddressdata()

# create the truck objects and set them with their respective initial conditions
truck1 = Truck(datetime.timedelta(hours=8), 0, [], '4001 South 700 East')
# load the truck based on given constraints
truck1.packages = [1, 13, 14, 15, 16, 19, 20, 21, 29, 30, 31, 34, 37, 40]

truck2 = Truck(datetime.timedelta(hours=9, minutes=5), 0, [], '4001 South 700 East')
# load the truck based on given constraints
truck2.packages = [2, 3, 4, 5, 6, 7, 8, 10, 11, 17, 18, 25, 26, 28, 36, 38]
# driver 1 switches from truck 1 to truck 3 after delivering truck 1's packages. Truck 1 is finished at 10:19 am
truck3 = Truck(datetime.timedelta(hours=10, minutes=20), 0, [], '4001 South 700 East')
# update package 9's address after 10:20 am
updated_package9 = Package(9, "410 S State St", "Salt Lake City", "UT", 84111, "EOD", packageHash.search(9).mass,
                           "At Hub")
packageHash.insert(9, updated_package9)  # insert and replace the original package 9 info with updated version
# load the truck based on the given constraints
truck3.packages = [9, 12, 22, 23, 24, 27, 32, 33, 35, 39]

# deliver truck 1's packages and save the ending time
end_time_truck1 = deliver_package(truck1, packageHash, address_data, distance_data)
# deliver truck 2's packages and save the ending time
end_time_truck2 = deliver_package(truck2, packageHash, address_data, distance_data)
# deliver truck 3's packages and save the ending time
end_time_truck3 = deliver_package(truck3, packageHash, address_data, distance_data)

# User Interface:
# The user interface options were inspired by the WGU Project Implementation Steps webpage

print("*****************************************")
print("Welcome to WGUPS Package Delivery Tracker")
print("Please Select An Option:")
print("Press 1 to Check All Package Status and Total Truck Mileage")
print("Press 2 to Get a Single Package Status With a Time")
print("Press 3 to Get All Package Status With a Time")
print("Press 4 to Exit")
print("*****************************************")

user_choice = int(input("Input: "))  # gets the users input

if (user_choice < 1) or (user_choice > 4):  # If the user input is not between 1 and 4 inclusive, this branch is taken
    print("Invalid Entry, Please Try Again")  # Prints out error message for invalid input
    user_choice = int(input("Input: "))  # Takes in a new user input
    while (user_choice < 1) or (user_choice > 4):  # Repeats the above so long as an invalid input is received
        print("Invalid Entry, Please Try Again")
        user_choice = int(input("Input: "))


while user_choice != 4:  # loops until the user selects 4 for exit

    if user_choice == 1:  # branch for user selection 1, prints all package status and truck mileage
        for i in range(1, 41):  # creates a loop that will iterate from 1 to 40, which are the package ID's
            package = packageHash.search(i)  # each pass of the loop will access the package object from the hash table
            # prints the package information
            print("Package ID: %d, " % i, "Address: " + str(package.address) + ", " + str(package.city) + ", " +
                  str(package.state) + ", " + str(package.zipcode) + ", " + str(package.mass) +" kg, STATUS: " +
                  str(package.current_status) + ", DEPART: " + str(package.depart_time) + ", ARRIVE: " +
                  str(package.arrive_time))
        # prints the individual trucks mileage as well as the total mileage
        print("Truck 1 Mileage: %d" % truck1.mileage)
        print("Truck 2 Mileage: %d" % truck2.mileage)
        print("Truck 3 Mileage: %d" % truck3.mileage)
        print("TOTAL MILEAGE: %d" % (truck1.mileage + truck2.mileage + truck3.mileage))
        user_choice = int(input("Input: "))  # gets new user input after the above loop is complete

    elif user_choice == 2:  # branches for user choice number 2, allowing a single package to be selected for given time
        user_choice_package = int(input("Enter the package ID for the package: "))  # gets ID of package to look up

        if user_choice_package >= 1 and user_choice_package <= 40:  # branches only if a valid ID is input
            user_choice_time_input = input("Enter the time to check (use format HH:MM:SS), ")  # asks user for time
            # use datetime's built in strptime to convert the input string to a time object
            # I learned about using this from: https://stackoverflow.com/questions/4628122/how-to-construct-a-timedelta
            # -object-from-a-simple-string
            user_choice_time = datetime.datetime.strptime(user_choice_time_input, "%H:%M:%S")
            # since the depart and arrive times of packages are time deltas, the user_choice_time must be converted
            # to a time delta for the comparison operators to work in the code that follows
            user_timedelta = datetime.timedelta(hours=user_choice_time.hour, minutes=user_choice_time.minute, seconds=
                                                user_choice_time.second)
            chosen_package = packageHash.search(user_choice_package)  # looks up the users chosen package

            # if the arrive time of the package is less than the users input time, then the package has arrived
            if chosen_package.arrive_time <= user_timedelta:
                print("Package ID: %d, " % user_choice_package, "Address: " + str(chosen_package.address) + ", " +
                      str(chosen_package.city) + ", " + str(chosen_package.state) + ", " + str(chosen_package.zipcode) +
                      ", " + str(chosen_package.mass) + " kg, STATUS: " + str(chosen_package.current_status) +
                      ", DEPART: " + str(chosen_package.depart_time) + ", ARRIVE: " + str(chosen_package.arrive_time))

                user_choice = int(input("Choose what to do next\n"
                                        "1 - Display all packages and truck mileage\n"
                                        "2 - Single package lookup for given time\n"
                                        "3 - All package display for given time\n"
                                        "4 - Exit the program\n"
                                        "Input: "))  # gets the next input from the user

            # if the arrive time is greater than the users input time, the package could be en route or at hub
            elif chosen_package.arrive_time > user_timedelta:
                # if the depart time is less than or equal to user input time, the package is en route
                if chosen_package.depart_time <= user_timedelta:
                    print("Package ID: %d, " % user_choice_package, "Address: " + str(chosen_package.address) + ", " +
                          str(chosen_package.city) + ", " + str(chosen_package.state) + ", " + str(
                        chosen_package.zipcode) + ", " + str(chosen_package.mass) + " kg, STATUS: En Route" +
                          ", DEPART: " + str(chosen_package.depart_time) + ", ARRIVE: " + "N/A")

                    user_choice = int(input("Choose what to do next\n"
                                            "1 - Display all packages and truck mileage\n"
                                            "2 - Single package lookup for given time\n"
                                            "3 - All package display for given time\n"
                                            "4 - Exit the program\n"
                                            "Input: "))  # gets the next input from the user

                # if the depart time is greater than the user input time, the package is still at the hub
                elif chosen_package.depart_time > user_timedelta:
                    print("Package ID: %d, " % user_choice_package, "Address: " + str(chosen_package.address) + ", " +
                          str(chosen_package.city) + ", " + str(chosen_package.state) + ", " + str(
                        chosen_package.zipcode) +
                          ", " + str(chosen_package.mass) + " kg, STATUS: At Hub" + ", DEPART: " +
                          str(chosen_package.depart_time) + ", ARRIVE: " + "N/A")

                    user_choice = int(input("Choose what to do next\n"
                                            "1 - Display all packages and truck mileage\n"
                                            "2 - Single package lookup for given time\n"
                                            "3 - All package display for given time\n"
                                            "4 - Exit the program\n"
                                            "Input: "))  # gets the next input from the user

        else:  # branches for invalid package ID
            while user_choice_package < 1 or user_choice_package > 40:  # loops as long as ID is invalid and gets new ID
                print("Invalid package ID")
                user_choice_package = int(input("Enter the package ID for the package: "))

    elif user_choice == 3:

        user_choice_time_input = input("Enter the time to check (use format HH:MM:SS), ")  # asks user for time
        # use datetime's built in strptime to convert the input string to a time object
        # I learned about using this from: https://stackoverflow.com/questions/4628122/how-to-construct-a-timedelta
        # -object-from-a-simple-string
        user_choice_time = datetime.datetime.strptime(user_choice_time_input, "%H:%M:%S")
        # since the depart and arrive times of packages are time deltas, the user_choice_time must be converted
        # to a time delta for the comparison operators to work in the code that follows
        user_timedelta = datetime.timedelta(hours=user_choice_time.hour, minutes=user_choice_time.minute, seconds=
        user_choice_time.second)

        for i in range(1, 41):  # creates a loop that will iterate from 1 to 40, which are the package ID's
            package = packageHash.search(i)  # each pass of the loop will access the package object from the hash table

            # if the arrive time of the package is less than the users input time, then the package has arrived
            if package.arrive_time <= user_timedelta:
                print("Package ID: %d, " % package.package_id, "Address: " + str(package.address) + ", " +
                      str(package.city) + ", " + str(package.state) + ", " + str(package.zipcode) +
                      ", " + str(package.mass) + " kg, STATUS: " + str(package.current_status) +
                      ", DEPART: " + str(package.depart_time) + ", ARRIVE: " + str(package.arrive_time))

            # if the arrive time is greater than the users input time, the package could be en route or at hub
            elif package.arrive_time > user_timedelta:

                # if the depart time is less than or equal to user input time, the package is en route
                if package.depart_time <= user_timedelta:
                    print("Package ID: %d, " % package.package_id, "Address: " + str(package.address) + ", " +
                          str(package.city) + ", " + str(package.state) + ", " + str(package.zipcode) + ", " +
                          str(package.mass) + " kg, STATUS: En Route" +", DEPART: " + str(package.depart_time) +
                          ", ARRIVE: " + "N/A")

                # if the depart time is greater than the user input time, the package is still at the hub
                elif package.depart_time > user_timedelta:
                    print("Package ID: %d, " % package.package_id, "Address: " + str(package.address) + ", " +
                          str(package.city) + ", " + str(package.state) + ", " + str(package.zipcode) +", " +
                          str(package.mass) + " kg, STATUS: At Hub" + ", DEPART: " + str(package.depart_time) +
                          ", ARRIVE: " + "N/A")

        user_choice = int(input("Choose what to do next\n"
                                "1 - Display all packages and truck mileage\n"
                                "2 - Single package lookup for given time\n"
                                "3 - All package display for given time\n"
                                "4 - Exit the program\n"
                                "Input: "))  # gets the next input from the user