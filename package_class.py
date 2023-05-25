#The purpose of this class is to create a package object to hold all the package data and also print out the info

class Package:
    # initialize the package object to hold all the info listed below for later access in the program
    # this class is a modification of what is seen in the WGU C950 Webinar 2 'Movie' class
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

    # the __str__ constructor allows us to print the package class as a string instead of a reference
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.package_id, self.address, self.city, self.state,
                                                           self.zipcode, self.deadline,
                                                           self.mass, self.current_status, self.depart_time,
                                                           self.arrive_time)

