import csv
import Package


def loadPackageData(file, hash_table):
    """
    Loads in the package data into the hash table.
    Big-O: O(n)
    """
    with open(file) as package_CSV:
        package_data = csv.reader(package_CSV, delimiter=',')
        next(package_data)
        for package in package_data:
            package_id = int(package[0])
            package_address = package[1]
            package_city = package[2]
            package_state = package[3]
            package_zip = str(package[4])
            package_deadline = str(package[5])
            package_weight = int(package[6])
            package_status = "At the hub."
            package_notes = package[7]

            package = Package.Package(package_id, package_address, package_city, package_state, package_zip,
                                      package_deadline,
                                      package_weight, package_status, package_notes)

            hash_table.insert(package_id, package)


def loadAddressData(address_data):
    """
    Loads in the address data to the address list (addressList).
    Big-O: O(n^2)
    """
    with open("AddressList.csv") as address_CSV:
        address_data_bucket = csv.reader(address_CSV, delimiter=',')
        for address in address_data_bucket:
            a = str(address)
            for i in a:
                if i.isdigit():
                    get_index = a.index(i)
                    break
            address = a[get_index:(len(a) - 2)]
            address_data.append(address)


def loadDistanceData(distance_data):
    """
    Loads in the distance data to the distance list (distanceList).
    Big-O: O(n^2)
    """
    with open("DistanceList.csv") as dis_CSV:
        dis_data = csv.reader(dis_CSV, delimiter=',')
        for distance in dis_data:
            list_a = list()
            for i in range(27):
                list_a.append(distance.__getitem__(i))
            distance_data.append(list_a)
