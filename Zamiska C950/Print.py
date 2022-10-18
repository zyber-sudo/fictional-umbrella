

def printAllPackages(hash_table):
    """
    Controls the printing of all the packages at the end of the day.
    Big-O: O(n)
    """
    txt = "***{0}***          ***{1}***                    ***{2}***          ***{3}***          ***{4}***          " \
          "***{5}***".format("PACKAGE ID", "PACKAGE ADDRESS", "PACKAGE DEADLINE", "DEPARTURE TIME", "DELIVERY TIME",
                             "STATUS")

    print(txt + "\n")
    for i in range(40):
        package_txt = "{:<28}{:<45}{:<31}{:<30}{:<25}{:<0}"
        print(package_txt.format(str(hash_table.search(i + 1).getPackageId()),
                                 str(hash_table.search(i + 1).getPackageAddress()),
                                 str(hash_table.search(i + 1).getPackageDeadline()),
                                 str(hash_table.search(i + 1).getHubTime()),
                                 str(hash_table.search(i + 1).getDeliveredTime()),
                                 hash_table.search(i + 1).getPackageStatus()))


def printPackageWithId(package_id, hash_table):
    """
    Controls the printing of a specific package (by id number) at the end of the day.
    Big-O: O(1)
    """
    txt = "***{0}***          ***{1}***                    ***{2}***          ***{3}***          ***{4}***          " \
          "***{5}***".format("PACKAGE ID", "PACKAGE ADDRESS", "PACKAGE DEADLINE", "DEPARTURE TIME", "DELIVERY TIME",
                             "STATUS")

    print(txt + "\n")

    package_txt = "{:<28}{:<45}{:<31}{:<30}{:<25}{:<0}"
    print(package_txt.format(str(hash_table.search(package_id).getPackageId()),
                             str(hash_table.search(package_id).getPackageAddress()),
                             str(hash_table.search(package_id).getPackageDeadline()),
                             str(hash_table.search(package_id).getHubTime()),
                             str(hash_table.search(package_id).getDeliveredTime()),
                             hash_table.search(package_id).getPackageStatus()))


def printAllPackageWithTime(time_input, hash_table):
    """
    Prints all the package information depending on a selected time.
    Big-O: O(n)
    """
    for i in range(40):
        if hash_table.search(i + 1).getDeliveredTime() < time_input:
            continue
        elif hash_table.search(i + 1).getHubTime() < time_input:
            hash_table.search(i + 1).setPackageStatus("IN TRANSIT")
            hash_table.search(i + 1).setDeliveredTime(None)
        else:
            hash_table.search(i + 1).setPackageStatus("AT HUB")
            hash_table.search(i + 1).setDeliveredTime(None)
            hash_table.search(i + 1).setHubTime(None)

    txt1 = "***{0}***          ***{1}***                    ***{2}***          ***{3}***          ***{4}***          " \
           "***{5}***".format("PACKAGE ID", "PACKAGE ADDRESS", "PACKAGE DEADLINE", "DEPARTURE TIME", "DELIVERY TIME",
                              "STATUS")

    print(txt1 + "\n")
    for i in range(40):
        package_txt = "{:<28}{:<45}{:<31}{:<30}{:<25}{:<0}"
        print(package_txt.format(str(hash_table.search(i + 1).getPackageId()),
                                 str(hash_table.search(i + 1).getPackageAddress()),
                                 str(hash_table.search(i + 1).getPackageDeadline()),
                                 str(hash_table.search(i + 1).getHubTime()),
                                 str(hash_table.search(i + 1).getDeliveredTime()),
                                 hash_table.search(i + 1).getPackageStatus()))


def printPackageWithIdAndTime(package_id, time_input, hash_table):
    """
    Controls the display and printing of the packages they are selected with an ID and a time.
    Big-O: O(n)
    """
    for i in range(40):
        if hash_table.search(i + 1).getDeliveredTime() < time_input:
            continue
        elif hash_table.search(i + 1).getHubTime() < time_input:
            hash_table.search(i + 1).setPackageStatus("IN TRANSIT")
            hash_table.search(i + 1).setDeliveredTime(None)
        else:
            hash_table.search(i + 1).setPackageStatus("AT HUB")
            hash_table.search(i + 1).setDeliveredTime(None)
            hash_table.search(i + 1).setHubTime(None)

    txt = "***{0}***          ***{1}***                    ***{2}***          ***{3}***          ***{4}***          " \
          "***{5}***".format("PACKAGE ID", "PACKAGE ADDRESS", "PACKAGE DEADLINE", "DEPARTURE TIME", "DELIVERY TIME",
                             "STATUS")

    print(txt + "\n")

    package_txt = "{:<28}{:<45}{:<31}{:<30}{:<25}{:<0}"
    print(package_txt.format(str(hash_table.search(package_id).getPackageId()),
                             str(hash_table.search(package_id).getPackageAddress()),
                             str(hash_table.search(package_id).getPackageDeadline()),
                             str(hash_table.search(package_id).getHubTime()),
                             str(hash_table.search(package_id).getDeliveredTime()),
                             hash_table.search(package_id).getPackageStatus()))
