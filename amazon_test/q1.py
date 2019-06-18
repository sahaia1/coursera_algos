def prioritizedOrders(numOrders, orderList):
    # WRITE YOUR CODE HERE
    def is_alphanumeric(x):
        _id, *metadata = x
        for c in metadata[0]:
            if ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord(
                    'A'):
                return True
        return False

    def sort_order(x):
        _id, *metadata = x
        return metadata, _id

    orderList.sort(key=sort_order)
    orderList.sort(key=is_alphanumeric, reverse=True)
    return orderList