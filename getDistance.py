# create a function that will return the distance between two locations

# takes in the distance data matrix and accesses the distance based on two indexes
def getdistance(distancedata, address1_index, address2_index):
    distance = distancedata[address1_index][address2_index]

    # due to the structure of the distance data, a blank may be found
    if distancedata[address1_index][address2_index] == '':
        # if blank is found, switching the row and column will access the distance
        distance = distancedata[address2_index][address1_index]

    return float(distance)  # return the distance as a float type to accommodate fractional values