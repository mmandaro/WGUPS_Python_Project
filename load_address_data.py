import csv


def load_address_data():
    """Function that takes the addresses from the address csv file and returns them as a list."""
    with open("WGUPS_Address_File.csv", 'r') as address_data_file:
        address_data_csv = csv.reader(address_data_file)
        address_data = list(address_data_csv)
        address_data[0][0] = '0'

        return address_data


