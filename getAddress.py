def get_address(address, address_data):
    """Function that will get the address numbers from the address data for use in get distance function."""

    # Iterate through each row of the address data
    for row in address_data:
        # While iterating, if the address matches, return index for that address
        if row[2] == address:
            # Return the address index as integer type
            return int(row[0])

