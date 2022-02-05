from typing import List


class QuickSort:
    """
    Quick Sort implementation
    """

    def quick_sort(self, data: List):
        """
        Sorts the data using quicksort
        """

        # Base case which returns the list if the size is equal to 1 or 2
        if len(data) < 2:
            return data

        pivot: int = data[0]

        numbers_less_than_pivot = [num for num in data[1:] if num < pivot]

        numbers_greater_than_pivot = [num for num in data[1:] if num > pivot]

        return (
            self.quick_sort(numbers_less_than_pivot)
            + [pivot]
            + self.quick_sort(numbers_greater_than_pivot)
        )
