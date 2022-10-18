# The Truck module
import datetime


class Truck:

    def __init__(self, truck_capacity=16, truck_packages=None):
        """
        The initialize function when a new truck is created.
        Big-O: O(n)
        """
        if truck_packages is None:
            truck_packages = []
        self.capacity = truck_capacity
        self.packages = truck_packages
        self.hub_time = datetime.timedelta(hours=int(8), minutes=int(0), seconds=int(0))
        self.date_time = datetime.timedelta(hours=int(8), minutes=int(0), seconds=int(0))
        self.mileage = int(0)
        self.current_address = None
        self.last_address = None

    def __str__(self):
        """
        Function that overrides the standard print function of the truck object.
        :return: The new format to print the truck.
        """
        return "Truck Capacity: " + str(self.capacity) + "\n" + "Packages in Truck: " + str(self.packages) + "\n" + \
               "Time left HUB: " + str(self.hub_time) + "\nFinish Time: " + str(self.date_time)

    def setDistance(self, dis):
        """Sets the trucks starting distance."""
        self.mileage = dis

    def setCurrentAddress(self, address):
        """Sets the trucks current address."""
        self.current_address = address

    def setlastAddress(self, address):
        """Sets the trucks previous address."""
        self.last_address = address

    def setHubTime(self, left_hub_at):
        """Sets the time the truck left the HUB."""
        self.hub_time = left_hub_at

    def setPackageTime(self, package_time):
        """Sets the trucks total delivery time."""
        self.date_time = package_time

    def getPackageTime(self):
        """Get the trucks total delivery time."""
        return self.date_time

    def getLastAddress(self):
        """Get the trucks previous address."""
        return self.last_address

    def getHubTime(self):
        """Get the trucks HUB departure time."""
        return self.hub_time

    def getCurrentAddress(self):
        """Get the trucks current address."""
        return self.current_address

    def getDistance(self):
        """Get the trucks distance."""
        return self.mileage

    def addDistance(self, dis):
        """Adds an amount of distance to the trucks total delivery mileage."""
        self.mileage += dis

    def addTime(self, time_to_add):
        """Add an amount of time to the trucks total time."""
        self.date_time += time_to_add
