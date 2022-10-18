# The Package module
import datetime


# The Package class
class Package:

    def __init__(self, package_id, package_address, package_city, package_state, package_zip, package_deadline,
                 package_weight, package_status, package_notes):
        """
        The initialize function when a new package is created.
        Big-O: O(n)
        """

        self.id = package_id
        self.address = package_address
        self.city = package_city
        self.state = package_state
        self.zip = package_zip
        self.deadline = package_deadline
        self.weight = package_weight
        self.status = package_status
        self.notes = package_notes
        self.delivered_time = datetime.timedelta(hours=int(8), minutes=int(0), seconds=int(0))
        self.hub_time = datetime.timedelta(hours=int(8), minutes=int(0), seconds=int(0))

    def __str__(self):
        """
        Function that overrides the standard print function of the Package object.
        :return: The new format to print the package.
        """
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.id, self.address, self.city, self.state, self.zip, self.deadline, self.weight,
            self.status, self.delivered_time, self.notes)

    # Getters for the Package object.
    def getPackageId(self):
        """
        Gets the Package ID.
        """
        return self.id

    def getPackageAddress(self):
        """
        Gets the Package address.
        """
        return self.address

    def getPackageDeadline(self):
        """
        Gets the Package deadline.
        """
        return self.deadline

    def getPackageCity(self):
        """
        Gets the Package city.
        """
        return self.city

    def getPackageZip(self):
        """
        Gets the Package zip code.
        """
        return self.zip

    def getPackageWeight(self):
        """
        Gets the Package weight.
        """
        return self.weight

    def getPackageStatus(self):
        """
        Gets the Package delivery status.
        """
        return self.status

    def getPackageNotes(self):
        """
        Gets the Package special notes.
        """
        return self.notes

    def getDeliveredTime(self):
        """
        Gets the Package time that it was delivered.
        """
        return self.delivered_time

    def getHubTime(self):
        """
        Gets the Package time it left the HUB.
        """
        return self.hub_time

    # Setters for the Package object.
    def setPackageAddress(self, package_address):
        """
        Sets the Package address.
        """
        self.address = package_address

    def setPackageZip(self, package_zip):
        """
        Sets the Package zip code.
        """
        self.zip = package_zip

    def setPackageStatus(self, status):
        """
        Sets the Package delivery status.
        """
        self.status = status

    def setDeliveredTime(self, pdt):
        """
        Sets the Package time it was delivered to destination.
        """
        self.delivered_time = pdt

    def setHubTime(self, left_hub_at):
        """
        Sets the Package time that it left the HUB.
        """
        self.hub_time = left_hub_at
