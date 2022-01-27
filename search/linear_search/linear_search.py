from typing import List


class LinearSearch:

    def __init__(self, data: List, item) -> None:

        """
        A class to search for item in an unordered list
        """

        self.data = data
        self.item = item

    def search(self):
        found: bool = False
        item_location: int = None

        for index, element in enumerate(self.data):

            if element == self.item:
                found = True
                item_location = index

        return item_location
