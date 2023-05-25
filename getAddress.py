# a function that will get the address numbers from the address data for use in get distance function

def getaddress(address, addressdata):
    for row in addressdata:  # iterate through each row of the address data
        if row[2] == address:  # while iterating, if the address matches, return number for that address
            return int(row[0])  # return the address number as integer type

