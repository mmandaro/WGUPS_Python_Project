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
        return f"Package {self.package_id}:\n" \
               f"Address: {self.address}, {self.city}, {self.state}, {self.zipcode}\n"\
               f"Deadline: {self.deadline}, Mass: {self.mass}\n" \
               f"Status: {self.current_status}, Depart Time: {self.depart_time}, Arrive Time: {self.arrive_time}\n"

