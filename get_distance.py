def get_distance(distance_data, address1_index, address2_index):
    """Function that will return the distance between two locations by accessing the data matrix."""

    # Acquires the distance from the distance matrix and assigns it to variable 'distance'
    distance = distance_data[address1_index][address2_index]

    # Due to the structure of the distance data, a blank may be found
    if distance_data[address1_index][address2_index] == '':

        # If blank is found, switching the row and column will access the distance
        distance = distance_data[address2_index][address1_index]

    # Return the distance as a float type to accommodate fractional values
    return float(distance)