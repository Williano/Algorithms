from typing import List


class SelectionSort:
    def __init__(self, data: List) -> None:
        self.data = data

    def find_smallest_number(self) -> int:

        # Set the smallest number to firs element in the list
        # Set the smallest number's index to the first
        smallest_number = self.data[0]
        smallest_number_index = 0

        # Go through the array from the second element since the
        # first element has been set as the smallest
        for element_index in range(1, len(self.data)):

            if self.data[element_index] < smallest_number:
                smallest_number = self.data[element_index]
                smallest_number_index = element_index

        return smallest_number_index

    def selection_sort(self) -> List:
        # Creates news list to store the sorted data
        new_list = []

        # Goes through the list and finds the smallest item
        # and add it to the new array.
        for element in range(len(self.data)):

            smallest_number_index = self.find_smallest_number()
            new_list.append(self.data.pop(smallest_number_index))

        return new_list
