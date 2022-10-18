
def distanceBetween(address1, address2, address_data, distance_data):
    """
    Gets the distance between two addresses in reference to the distance graph.
    As well as completing the second half of the bidirectional distance graph with the proper indexes.
    Uses the distance data list (distanceData)
    Returns the distance between in the form of a float.
    Big-O: O(1)
    """
    address1 = address_data.index(address1)
    address2 = address_data.index(address2)

    if address1 > address2:
        return float(distance_data[address1][address2])
    elif address1 < address2:
        return float(distance_data[address2][address1])
    else:
        return float(distance_data[address1][address2])


