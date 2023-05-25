import csv  # import the csv built in to be able to read in the csv files

from package_class import Package


# a function to load the package data from the csv file
# The following method is an adaptation of what is used in WGU C950 Webinar 2, the loadMovieData function

def loadpackagedata(chainingHash):
    with open("WGUPS_Package_File.csv", 'r') as packagedata_file:
        # reading in the csv package file data and assigning it to package_data
        package_data_csv = csv.reader(packagedata_file)  # uses csv reader to read the package data
        package_data = list(package_data_csv)  # makes the package data into a list so we can iterate over it
        package_data = package_data[2:-7]  # slices off extraneous data from beginning and end (header & blanks)

        for package_row in package_data:  # iterates through each row of the package data
            package_id = int(package_row[0])  # sets the package ID
            address = package_row[1]  # sets the package address
            city = package_row[2]  # sets the package city
            state = package_row[3]  # sets the package state
            zipcode = package_row[4]  # sets the package zipcode
            deadline = package_row[5]  # sets the package deadline
            mass = package_row[6]  # sets the weight of the package
            status = 'At Hub'  # initializes status to at hub

            # create a package object using the package class and the variables saved above
            package = Package(package_id, address, city, state, zipcode, deadline, mass, status)

            #insert package into the hashtable, with package_id as the key, and package as the item
            chainingHash.insert(package_id, package)
