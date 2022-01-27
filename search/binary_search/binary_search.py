class BinarySearch:
    def __init__(self, data, item) -> None:

        self.data = data
        self.item = item

    def binary_search(self):

        low = 0
        high = len(self.data) - 1

        while low <= high:

            middle_number_index = (low + high) // 2
            guess = self.data[middle_number_index]

            if guess == self.item:
                return middle_number_index

            if guess > self.item:
                high = middle_number_index - 1

            else:
                low = middle_number_index + 1

        return None
