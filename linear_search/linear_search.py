def linear_search(data, item):

    found: bool = False
    item_location: int = None

    for index, element in enumerate(data):

        if element == item:
            found = True
            item_location = index

    return item_location
