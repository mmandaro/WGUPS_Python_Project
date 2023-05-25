# creates the truck object to organize information regarding the delivery trucks
# this class is a modification of what is seen in the WGU C950 Webinar 2 'Movie' class
class Truck:

    def __init__(self, depart_time, mileage, packages, address, carry_max = 16, speed = 18):
        self.depart_time = depart_time  # what time the truck departs the hub
        self.mileage = mileage  # the mileage of the truck for the day
        self.packages = packages  # the packages on the truck
        self.address = address  # the current address of the truck, starting at the hub
        self.carry_max = carry_max  # each truck may carry a max of 16 packages
        self.speed = speed  # the trucks travel on avg 18 mph as given in task instructions

# allows truck information to be printed out instead of a reference
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s" % (self.depart_time, self.mileage, self.packages, self.address, self.carry_max,
                                           self.speed)




