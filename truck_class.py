class Truck:
    """Creates the truck object to organize and group information regarding delivery trucks."""
    def __init__(self, depart_time, mileage, packages, address, carry_max=16, speed=18):
        # What time the truck departs the hub
        self.depart_time = depart_time
        # The mileage of the truck for the day
        self.mileage = mileage
        # The packages on the truck
        self.packages = packages
        # The current address of the truck, starting at the hub
        self.address = address
        # Each truck may carry a max of 16 packages
        self.carry_max = carry_max
        # The trucks travel on avg 18 mph as given in task instructions
        self.speed = speed

    def __str__(self):
        """Allows the truck attributes to be printed neatly."""
        return f"Depart Time: {self.depart_time}, Mileage: {self.mileage}, Packages: {self.packages}"\
               f"Address: {self.address}, Carry Max: {self.carry_max,}, Speed: {self.speed}"





