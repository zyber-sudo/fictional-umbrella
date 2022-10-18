"""
First Name: Zachary
Last Name: Zamiska
Student ID: 003194341

NOTE: To correctly run the program please start with MainMenu.py
"""

# Imports from other modules.
import datetime
import math
import Hash
import Load

import Truck
from DistanceCalc import distanceBetween

# Global variable initialization.

# List to input the distance data
distanceData = list()

# List to input the address data into.
addressData = list()

# Package hash table creation. (Using the hash module)
package_hash_table = Hash.ChainingHashTable()


def truckLoadPackages():
    """
    Loads the packages onto the truck.
    NOTE: The packages are loaded heuristically for the sake of easy adjustment.
    This could be an area that can be improved (See section J).
    Big-O: O(1)
    """

    truck_1.packages.append(package_hash_table.search(1))
    truck_1.packages.append(package_hash_table.search(37))
    truck_1.packages.append(package_hash_table.search(40))
    truck_1.packages.append(package_hash_table.search(5))
    truck_1.packages.append(package_hash_table.search(25))
    truck_1.packages.append(package_hash_table.search(8))
    truck_1.packages.append(package_hash_table.search(10))
    truck_1.packages.append(package_hash_table.search(11))
    truck_1.packages.append(package_hash_table.search(12))
    truck_1.packages.append(package_hash_table.search(13))
    truck_1.packages.append(package_hash_table.search(14))
    truck_1.packages.append(package_hash_table.search(15))
    truck_1.packages.append(package_hash_table.search(16))
    truck_1.packages.append(package_hash_table.search(17))
    truck_1.packages.append(package_hash_table.search(19))
    truck_1.packages.append(package_hash_table.search(20))

    truck_2.packages.append(package_hash_table.search(3))
    truck_2.packages.append(package_hash_table.search(18))
    truck_2.packages.append(package_hash_table.search(21))
    truck_2.packages.append(package_hash_table.search(22))
    truck_2.packages.append(package_hash_table.search(23))
    truck_2.packages.append(package_hash_table.search(24))
    truck_2.packages.append(package_hash_table.search(26))
    truck_2.packages.append(package_hash_table.search(7))
    truck_2.packages.append(package_hash_table.search(29))
    truck_2.packages.append(package_hash_table.search(30))
    truck_2.packages.append(package_hash_table.search(31))
    truck_2.packages.append(package_hash_table.search(6))
    truck_2.packages.append(package_hash_table.search(34))
    truck_2.packages.append(package_hash_table.search(35))
    truck_2.packages.append(package_hash_table.search(36))
    truck_2.packages.append(package_hash_table.search(38))

    truck_3.packages.append(package_hash_table.search(33))
    truck_3.packages.append(package_hash_table.search(27))
    truck_3.packages.append(package_hash_table.search(9))
    truck_3.packages.append(package_hash_table.search(28))
    truck_3.packages.append(package_hash_table.search(32))
    truck_3.packages.append(package_hash_table.search(2))
    truck_3.packages.append(package_hash_table.search(39))
    truck_3.packages.append(package_hash_table.search(4))


def minDistanceFrom(from_address, truck):
    """
    Takes an address (from_address) and loops through the packages in the truck (truck_packages) to find the
    closet one next.
    Uses the distanceBetween() function for the distance between addresses. Returns the package (obj)
    that is the closest to the address given (from_address).
    Big-O: O(n)

    :return: Package that is the closest the address given.
    :param from_address: Address of the package that is needed to find the closest next package.
    :param truck: Truck that is used to iterate through all the packages loaded.


    Big-O: O(n)
    """

    # Sets the minimum distance to a much higher magnitude than the minimum value resetting the variable for each truck.
    min_distance = float(100)

    # Iterates through the truck that was given as a parameter, getting the address of each package (package_address)
    # and comparing it to the address given (from_address) using the distanceBetween() function.
    for j in truck.packages:
        package_address = j.getPackageAddress()
        current_distance = distanceBetween(from_address, package_address, addressData, distanceData)
        if current_distance < min_distance:
            # Once the minimum distance (min_distance) is found, the package to which the address belongs to is
            # assigned to obj to be returned.
            min_distance = current_distance
            obj = j

    # The following actions are ran after the closest package (obj) is found using the minimum distance (min_distance)

    # Adds the distance using the minimum distance (min_distance) variable to the trucks total mileage.
    truck.addDistance(min_distance)

    # Using the timeLogic() function to do the proper calculations, the amount of time to drive the minimum distance
    # (min_distance) is added to the trucks time. Effectively having the truck "drive" to the address.

    # NOTE: The actual package is not removed until the truckDeliverPackages() function.
    truck.addTime(timeLogic(min_distance))

    # Package that is being returned.
    return obj


def truckDeliverPackages(truck):
    """
    Function that delivers the packages depending on the truck given as a parameter.

    :param truck: Truck that will have the packages delivered.

    Big-O: O(n^2)
    """

    # Sets the trucks current address to WGU
    initial_address = "4001 South 700 East"
    truck.setCurrentAddress(initial_address)
    hub_time = truck.getHubTime()
    for pack in truck.packages:
        pack.setHubTime(hub_time)

    # Gets the minimum distance from WGU
    package = minDistanceFrom(truck.getCurrentAddress(), truck)
    # Sets the objects status to delivered, seeing as the truck has arrived at the packages'
    # destination (i.e. Starting the Unpacking).
    package.setPackageStatus("DELIVERED")
    # Sets the package delivered time to the time the truck "arrived" at the address.
    # Effectively finishing the delivery.
    package.setDeliveredTime(truck.date_time)

    truck.setlastAddress(truck.getCurrentAddress())
    truck.setCurrentAddress(package.getPackageAddress())

    truck.packages.remove(package)

    while len(truck.packages) != 0:
        for pack in truck.packages:
            pack.setPackageStatus("IN TRANSIT")

            # Gets the package that is the minimum distance from the current point.
            package = minDistanceFrom(truck.getCurrentAddress(), truck)
            # Sets the objects status to delivered, seeing as the truck has arrived at the packages'
            # destination (i.e. Starting the Unpacking).
            package.setPackageStatus("DELIVERED")
            # Sets the package delivered time to the time the truck "arrived" at the address.
            # Effectively finishing the delivery.
            package.setDeliveredTime(truck.date_time)

            truck.setlastAddress(truck.getCurrentAddress())
            truck.setCurrentAddress(package.getPackageAddress())

            truck.packages.remove(package)


def truckDepartureController():
    """
    Controls the departure time for each truck. This also runs the truckDeliverPackages() function for each truck.
    Big-O: O(n)
    """
    truckDeliverPackages(truck_1)

    # Delays the departure of the 2nd truck due to the constraints from the delayed packages.
    truck_2.setHubTime(datetime.timedelta(hours=int(9), minutes=int(5), seconds=int(0)))
    truckDeliverPackages(truck_2)

    # Determines what truck returns to the HUB because that is the only mileage that matters.
    # This is because the other driver has no other obligations.
    if truck_1.date_time < truck_2.date_time:
        truck_1.addDistance(distanceBetween(truck_1.current_address, "4001 South 700 East", addressData, distanceData))
    else:
        truck_2.addDistance(distanceBetween(truck_1.current_address, "4001 South 700 East", addressData, distanceData))

    # Delays the final truck and corrects the address of the incorrectly labeled package #9.
    truck_3.hub_time = datetime.timedelta(hours=int(10), minutes=int(20), seconds=int(0))
    truck_3.date_time = datetime.timedelta(hours=int(10), minutes=int(20), seconds=int(0))
    package_hash_table.search(9).setPackageAddress("410 S State St")
    package_hash_table.search(9).setPackageZip("84111")

    truckDeliverPackages(truck_3)


def timeLogic(dis, mph=18):
    """
    Provides the logic to calculate the amount of time a distance requires.

    :param dis: The distance (in miles) that will be used to calculate the amount of delivery time.
    :param mph: The speed of which the truck will travel.
    :return: Time to add to any datetime object.

    Big-O: O(1)
    """

    time = dis / mph

    hour = math.floor(time)
    minute = (time % 1) * 60
    sec = int((minute % 1) * 60)

    # Returns the amount of time a distance takes to add to datetime object.
    return datetime.timedelta(hours=int(hour), minutes=int(minute), seconds=int(sec))


Load.loadPackageData("WGUPSPackageFile.csv", package_hash_table)
Load.loadDistanceData(distanceData)
Load.loadAddressData(addressData)
truck_1 = Truck.Truck()
truck_2 = Truck.Truck()
truck_3 = Truck.Truck()
truckLoadPackages()
truckDepartureController()

