import csv  # imports pythons built in csv module so we can open and read files

# this function takes the addresses from the address csv file and returns it as a list
def loadaddressdata():
    with open("WGUPS_Address_File.csv", 'r') as addressdata_file:
        addressdata_csv = csv.reader(addressdata_file)
        addressdata = list(addressdata_csv)
        addressdata[0][0] = '0'

        return addressdata


