import csv


def load_distance_data():
    """Function that will open the csv file, make it a list and return the variable containing this list."""

    # Open the csv file with read privileges
    with open("WGUPS_Distance_File.csv", 'r') as distance_data_file:
        # Assign the data to a variable
        distance_data_csv = csv.reader(distance_data_file)
        # Make the distance data into a list
        distance_data = list(distance_data_csv)
        # Fixes formatting issue by replacing /ueff0 with just 0, as intended
        distance_data[0][0] = '0'

        return distance_data

