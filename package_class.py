class Package:
    """Creates package objects to group all package data in one place."""
    def __init__(self, package_id, address, city, state, zipcode, deadline, mass, current_status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.mass = mass
        self.current_status = current_status
        self.depart_time = None
        self.arrive_time = None

    def __str__(self):
        """Allows package information to be printed neatly."""
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.package_id, self.address, self.city, self.state,
                                                           self.zipcode, self.deadline,
                                                           self.mass, self.current_status, self.depart_time,
                                                           self.arrive_time)

